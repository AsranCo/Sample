import pymysql
from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Alirez@123'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def hello():
    return "Welcome to Python Flask!"


@app.route('/signUp')
def index():
    return render_template('signUp.html')


@app.route('/process', methods=['POST'])
def process():
    # connect
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    email = request.form['email']

    if name and email and username and password:
        cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s)',
                       (name, username, password, email))
        conn.commit()
        msg = 'You have successfully registered!'
        return jsonify({'name': msg})

    return jsonify({'error': 'Missing data!'})


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
