from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "myLittleSecret"

@app.route("/")
session['count'] = 0
def init():

    return render_template("index.html", count = session['count'])