from flask import Flask,redirect,url_for,render_template,request
import os
import psycopg2
import subprocess

from httplib2 import Authentication

app = Flask(__name__)


@app.route("/")
def home():
    return ("Welcome")


@app.route("/signal")
def signal():
    return(subprocess.check_output('gammu-smsd-monitor -n 1 -d 0.5 | egrep -o \'NetworkSignal.+\'',shell = True))


@app.route("/count")
def count():
    con = psycopg2.connect(user='gammu',password='a',host='127.0.0.1',port='5432',database="smsd")
    con.autocommit = True
    cursor = con.cursor()
    post = "select * from outbox"
    cursor.execute(post)
    y = "Number of unsent SMS: " + str(cursor.rowcount)
    return (y)
    con.commit()
    con.close()



@app.route("/sms",methods=["POST","GET"])
def sms():
    con = psycopg2.connect(user='gammu',password='a',host='127.0.0.1',port='5432',database="smsd")
    con.autocommit = True
    cursor = con.cursor()
    post = "select * from loginweb"
    cursor.execute(post)
    mm = cursor.fetchall()
    status = "0"
    for row in mm:
        list.append(Authentication(str(row[2]),str(row[3])))
    if request.method == "POST":
        for x in list:
            if x.user == (request.authorization.username) and x.password == (request.authorization.password):
                status = "1"
        #   else:
        #       return ((request.authorization.username) + str(request.authorization.password))
        if status == "1" :
            return str(request.form["text"])
            array = str(request.form["number"]).split(",")
            for y in array:
                os.system('gammu-smsd-inject TEXT ' + str(y) + ' -unicode -textutf8 "' + str(request.form["text"]) + '"')
            return ("OK")
        else:
            return ("WRONG UserName OR Password")
    else:
        for x in list:
            if x.user == request.args.get("User") and x.password == request.args.get("Password"):
                status = "1"
        if status == "1" :

            array = str(request.args.get("Number")).split(",")

            for y in array:
                os.system('gammu-smsd-inject TEXT ' + str(y) + ' -unicode -textutf8 "' + str(request.args.get("Message")) + '"')
            return ("OK")
        else:
            return ("Wrong UserName OR Password")
    con.comit()
    con.close()


if __name__ == "__main__":
    app.run(host='192.168.154.10')
