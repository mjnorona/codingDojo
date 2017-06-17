import re, md5, os, binascii
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'login')
app.secret_key = "secretKey"
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

                query2 = "SELECT id FROM users WHERE email = :newEmail"
                data2 = { 'newEmail': request.form['email']}
                userID = mysql.query_db(query2,data2)

                session['id'] = userID[0]['id']

                return redirect("/wall")
        else:
            return render_template("index.html", invalid = True)
    else:
        redirect("/")

@app.route('/login', methods = ['POST'])
def login():
    if request.form['action'] == 'login':
        try:
            query = "SELECT password FROM users WHERE users.email = :specific_email"
            data = {"specific_email": request.form['email']}
            password = mysql.query_db(query,data)
            if md5.new(request.form['password']).hexdigest() == password[0]['password']:
                query2 = "SELECT id FROM users WHERE email = :newEmail"
                data2 = {'newEmail': request.form['email']}
                userID = mysql.query_db(query2, data2)

                session['id'] = userID[0]['id']
                return redirect("/wall")

        except IndexError:
            return render_template("index.html", log=True)

    else:
        return redirect("/")

@app.route("/wall")
def wall():
    user = 'SELECT first_name FROM users WHERE users.id = :userid'
    if "id" in session:
        userData = { 'userid': session['id']}
        username = mysql.query_db(user, userData)

        join = 'SELECT concat(users.first_name, " ", users.last_name) AS name, messages.content, concat(monthname(messages.created_at)," ", day(messages.created_at), ", ", year(messages.created_at)) as date, messages.id FROM users JOIN messages on users.id = messages.users_id ORDER BY messages.created_at DESC'
        data = { 'id': session['id']}
        myData = mysql.query_db(join, data)


        commentsData = 'SELECT concat(users.first_name, " ", users.last_name) as name, comments.content, concat(monthname(comments.created_at)," ", day(comments.created_at), ", ", year(comments.created_at)) as date, comments.messages_id FROM comments JOIN users ON comments.users_id = users.id'
        comments = mysql.query_db(commentsData)
        # return str(comments[0])
        return render_template("wall.html",messages = myData, comments = comments, username = username[0]['first_name'])
    else:
        return redirect("/")

@app.route("/message", methods = ["POST"])
def message():
    if request.form['action'] == "post":
        query = "INSERT INTO messages (content, created_at, updated_at, users_id) VALUES (:content, NOW(), NOW(), :id)"
        data = {
                    'content': request.form['message'],
                    'id': session['id']
                }
        mysql.query_db(query, data)
        return redirect("/wall")
    else:
        return redirect("/wall")

@app.route("/comment", methods = ["POST"])
def comment():
    messageID = request.form['action']
    query = 'INSERT INTO comments (content, created_at, updated_at, users_id, messages_id) VALUES (:content, NOW(), NOW(), :userID, :messageID);'
    data = {
                'content': request.form['message'],
                'userID': session['id'],
                'messageID': messageID
            }
    mysql.query_db(query, data)

    return redirect("/wall")

@app.route("/logout")
def logout():
    session.pop('id', None)
    return redirect("/")
app.run(debug=True)


