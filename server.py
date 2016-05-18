from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]+$')

app = Flask(__name__)
app.secret_key = "AltoidsMindsJar!"

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
	if len(request.form['email']) < 1: 
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")		

	elif len(request.form['first']) < 1:
		flash("First Name cannot be blank!")	
	elif len(request.form['last']) < 1:
		flash("Last Name cannot be blank!")	
	elif len(request.form['password']) < 8:
		flash("Password cannot be blank or less than 8 characters!")
	elif len(request.form['confirm']) < 1: 
		flash("Password Confirm cannot be blank!")	
	elif not NAME_REGEX.match(request.form['first']):
		flash("Name Cannot Have Numbers!")	
	elif not NAME_REGEX.match(request.form['last']):
		flash("Name Cannot Have Numbers!")			

	elif request.form['password'] != request.form['confirm']:
		flash("Passwords Don't Match!")

	else: 
		flash("Successfully Registered!")
		session['email'] = request.form['email']
		session['first'] = request.form['first']
		session['last'] = request.form['last']
		session['password'] = request.form['password']
		session['confirm'] = request.form['confirm']

	return redirect('/')
		


app.run(debug=True)				