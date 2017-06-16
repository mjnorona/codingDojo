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
        select = "SELECT email FROM users WHERE users.email = :specific_email"
        dataCheck = {"specific_email": request.form['email']}
        check = mysql.query_db(select, dataCheck)

        try:
            if check[0]['email'] == request.form['email']:
                return render_template("index.html", exists =1)
        except IndexError:
            query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
            data = {
                'email': request.form['email']
            }
            mysql.query_db(query, data)

            query2 = "SELECT * FROM users"
            list = mysql.query_db(query2)
            return render_template("success.html", list=list, input=request.form['email'])
    else:
        return render_template("index.html", invalid = 1)

app.run(debug=True)