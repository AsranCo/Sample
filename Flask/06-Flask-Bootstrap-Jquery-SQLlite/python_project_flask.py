from flask import Flask, render_template, request
import sqlite3 as sql
import pymonetdb
import cx_Oracle

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/enternew')
def enternew():
   return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         con.close()
         return render_template("result.html",msg = msg)

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

@app.route('/listMonetDB')
def listMonetDB():
   con = pymonetdb.connect(username="", password="", hostname="", port="", database="")
   cur = con.cursor()
   cur.execute("select avp_key,attr_value from \"TABLE\" ")
   rows = cur.fetchall()
   return render_template("listMonetDB.html",rows = rows)

@app.route('/listOracleDB')
def listOracleDB():
   con = cx_Oracle.connect("user/Pass@server:port/servicename")
   cur = con.cursor()
   cur.execute("SELECT DISTINCT  S.SOLTN_ABBR, LGCL_DM_NAME,CLIENT_SHORT_NAME, A.SPEC_ID,  A.SOLTN_PRCS_OPTION_ID,  MRT_DATA_PRCS_NAME, A.REFRESH_FREQUENCY, E.WEEKLY_UPDATE_FLG, E.PERIOD_REFRESH_SCHED FROM CLIENT_SOLTN_PRCS_OPTION A, MDM_CLIENT_MAP B, SOLTN_PRCS_OPTION C, MRT_DATA_PRCS D, CLIENT_SOLTN_SCHED E, LGCL_DM F, SOLTN S WHERE A.SOLTN_ID                = S.SOLTN_ID AND S.SOLTN_ID                = E.SOLTN_ID AND A.CLIENT_ID             = B.CLIENT_ID AND A.CLIENT_ID               = E.CLIENT_ID AND A.SOLTN_ID                = E.SOLTN_ID AND A.SOLTN_PRCS_OPTION_ID    = C.SOLTN_PRCS_OPTION_ID  AND C.MRT_DATA_PRCS_ID        = D.MRT_DATA_PRCS_ID AND A.LGCL_DM_ID              = F.LGCL_DM_ID AND A.SPEC_ID                 = E.SPEC_ID AND A.IS_REQUIRED=1 AND E.IS_REQUIRED=1 AND LGCL_DM_abbr LIKE  '%M' ORDER BY S.SOLTN_ABBR,LGCL_DM_NAME,CLIENT_SHORT_NAME,A.SPEC_ID, MRT_DATA_PRCS_NAME ")
   
   rows = cur.fetchall()
   return render_template("listOracleDB.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
