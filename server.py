from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
	def get(self):
		conn = db_connect.connect()  # connect database
		query =  conn.execute("SELECT * FROM employees") # execute query and return json result
		return {
			'data' : [
				dict(zip(tuple(query.keys()), i))
					for i in query.cursor
			]
		}

	def post(self):
		conn = db_connect.connect()
		print(request.json)

		lastName = request.json['last_name']
		firstName = request.json['first_name']
		title = request.json['title']
		reportTo = request.json['reports_to']
		birthDate = request.json['birth_date']
		hireDate = request.json['hire_date']
		address = request.json['address']
		city = request.json['city']
		state = request.json['state']
		country = request.json['country']
		postalCode = request.json['postal_code']
		phone = request.json['phone']
		fax = request.json['fax']
		email = request.json['email']

		query = conn.execute("INSERT INTO employees values(null, '{0}','{1}','{2}','{3}','{4}','{5}',\
			'{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')"
				.format(lastName, firstName, title, reportTo, birthDate, hireDate, address,city,state,
					country, postalCode, phone, fax, email))

		return {'status' : 'success'}

class Tracks(Resource):
	def get(self):
		conn = db_connect.connect()
		query = conn.execute("SELECT trackid, name, composer, unitprice FROM tracks")
		result = {
			'data' : [
				dict(zip(tuple(query.keys()), i))
					for i in query.cursor
			]
		}
		return result

class Employess_Name(Resource):
	def get(self, employee_id):
		conn = db_connect.connect()
		query = conn.execute("SELECT * FROM employees WHERE employeeid = %d" %int(employee_id))
		result = {
			'data' :
				dict(zip(tuple(query.keys()), i))
					for i in query.cursor
		}
		return result

api.add_resource(Employees, '/employees')
api.add_resource(Tracks, '/tracks')
api.add_resource(Employess_Name, '/employees/<employee_id>')

if __name__ == '__main__':
	#app.run()
	app.run(port='5002')