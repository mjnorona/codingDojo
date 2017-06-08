from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods = ["POST"])
def showResults():

    return render_template("result.html", name = request.form["name"], location = request.form["location"], language = request.form["language"], comment = request.form["comment"])
app.run(debug=True)