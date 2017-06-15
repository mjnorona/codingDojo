import re
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def init():
    return render_template("index.html")

@app.route('/submit', methods = ["POST"])
def submit():
    if EMAIL_REGEX.match(request.form['email']):
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
                    'email' : request.form['email']
                }
        mysql.query_db(query, data)

        query2 = "SELECT * FROM users"
        list = mysql.query_db(query2)
        return render_template("success.html", list= list, input = request.form['email'])
    else:
        return render_template("index.html", invalid = 1)

app.run(debug=True)