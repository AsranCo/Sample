import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/addEmployee', methods=['POST'])
def add_employee():
	try:
		_json = request.json
		_id =_json['id']
		_name = _json['name']
		_email = _json['email']
		_salary =_json['salary']
		# validate the received values
		if _id and _name and _email and _salary and request.method == 'POST':
			# save edits
			sql = "INSERT INTO employee(id, uname, email,salary) VALUES(%s, %s, %s ,  %s)"
			data = (_id, _name, _email,_salary)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Employee added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/employeeList')
def employees():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM employee")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/employee/<int:id>')
def employee(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM employee WHERE id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/employeeUpdate', methods=['POST'])
def update_employee():
	try:
		_json = request.json
		_id =_json['id']
		_name = _json['name']
		_email = _json['email']
		_salary =_json['salary']		
		# validate the received values
		if _id and _name and _email and _salary and request.method == 'POST':
			# save edits
			sql = "UPDATE employee SET uname=%s, email=%s, salary=%s WHERE id=%s"
			data = (_name, _email, _salary, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Employee updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<int:id>')
def delete_employee(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM employee WHERE id=%s", (id,))
		conn.commit()
		resp = jsonify('Employee deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run()