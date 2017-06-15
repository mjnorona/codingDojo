import re, md5, os, binascii
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'login')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def hasNumbers(input):
    for i in input:
        if i.isdigit():
            return True
    return False

@app.route('/')
def init():
    return render_template("index.html")

@app.route('/register', methods = ['POST'])
def register():
    if request.form['action'] == 'register':
        if (hasNumbers(request.form['first']) == False and len(request.form['first']) >= 2
            and hasNumbers(request.form['last']) == False and len(request.form['last']) >= 2
            and EMAIL_REGEX.match(request.form['email']) and request.form['email'] > 0
            and len(request.form['password']) >= 8 and request.form['password'] == request.form['confirm']):
            select = "SELECT email FROM users WHERE users.email = :specific_email"
            dataCheck = {"specific_email": request.form['email']}
            check = mysql.query_db(select, dataCheck)
            try:
                if check[0]['email'] == request.form['email']:
                    return render_template("index.html", exists = True)
            except IndexError:
                salt = binascii.b2a_hex(os.urandom(15))
                query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first, :last, :email, :password, NOW(), NOW())"
                data = {
                            "first": request.form['first'],
                            "last": request.form['last'],
                            "email": request.form['email'],
                            "password": md5.new(request.form['password']).hexdigest()
                        }
                mysql.query_db(query, data)
                print request.form['first']

                return redirect("/success")
        else:
            return render_template("index.html", invalid = True)
    else:
        redirect("/")

@app.route('/login', methods = ['POST'])
def login():
    if request.form['action'] == 'login':
        query = "SELECT password FROM users WHERE users.email = :specific_email"
        data = {"specific_email": request.form['email']}
        password = mysql.query_db(query,data)
        if md5.new(request.form['password']).hexdigest() == password[0]['password']:
            return redirect("/success")
        else:
            return render_template("index.html", log = True)
    else:
        return redirect("/")

@app.route("/success")
def success():
    return render_template("success.html")
app.run(debug=True)