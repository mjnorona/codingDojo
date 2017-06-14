from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def init():
    return render_template("index.html")

@app.route("/ninja")
def tmnt():
    return render_template("ninja.html")

@app.route("/ninja/<filename>")
def turtle(filename):
    if  filename == "purple":
        filename = "donatello"
    elif filename == "blue":
        filename = "leonardo"
    elif filename == "red":
        filename = "raphael"
    elif filename == "orange":
        filename = "michelangelo"

    if filename == "donatello" or filename == "leonardo" or filename == "michelangelo" or filename == "raphael":


        return render_template("certainNinja.html", filename = filename)
    else:
        return render_template("certainNinja.html", filename = "notapril")
app.run(debug=True)
