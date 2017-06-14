from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "myLittleSecret"

def sumSessionCounter():
    try:
        session['count'] += 1
    except KeyError:
        session['count'] = 1


@app.route("/")
def init():
    sumSessionCounter()
    return render_template("index.html", count = session['count'])

@app.route("/2count")
def double():
    sumSessionCounter()
    sumSessionCounter()
    return redirect("/")

@app.route("/reset")
def reset():
    session['count'] = 0
    print session['count']
    return redirect("/")

app.run(debug=True)