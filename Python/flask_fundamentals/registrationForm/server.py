import re
from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "secret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def hasNumbers(input):
    for i in input:
        if i.isdigit():
            return True
    return False


@app.route("/")
def init():
    return render_template("index.html")

@app.route("/submit", methods = ["POST"])
def showResults():
    if len(request.form["email"]) < 1 or len(request.form["firstName"]) < 1 or len(request.form["lastName"]) < 1 or len(request.form["password"]) < 1 or len(request.form["confirm"]) < 1:
        flash("All fields must be filled")
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email address")
    elif len(request.form["password"]) <= 8:
        flash("Password must be more than 8 characters")
    elif hasNumbers(request.form["firstName"]) or hasNumbers(request.form["lastName"]):
        flash("First and Last name cannot contain numbers")
    elif request.form["password"] != request.form["confirm"]:
        flash("Passwords do not match")
    else:
        flash("Thanks for submitting your information")
    return redirect("/")

app.run(debug=True)