from flask import Flask, render_template, redirect, request, flash, session

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods = ["POST"])
def showResults():
    if len(request.form["name"]) < 1:
        flash("Name cannot be empty")
        return redirect("/")
    elif len(request.form["comment"]) < 1:
        flash("Comment cannot be empty")
        return redirect("/")
    elif len(request.form["comment"]) > 120:
        flash("Comment can be no longer than 120 characters")
        return redirect("/")


    return render_template("result.html", name = request.form["name"], location = request.form["location"], language = request.form["language"], comment = request.form["comment"])
app.run(debug=True)