from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector 
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'EmailVal')

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'thisissecret'


@app.route('/', methods=['GET'])
def index():
	query="SELECT * FROM  emails"
	x=mysql.query_db(query)
	print x
	return render_template('index.html', emails=x)


@app.route('/emailVal', methods=['POST'])
def create():
	email=request.form['email']

	if len(request.form['email']) < 1:
		flash("Blank_Email") 
	elif not  EMAIL_REGEX.match(request.form['email']):
		flash("Invalid_Email")
	else:
		flash("Success")
		 # The email address you entered {}.format(request.form['name'] is a VALID email id.Thank You!")
		query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
		data = {
				'email': request.form['email']
				}

		mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)


