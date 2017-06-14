import random, time
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "FindTheGold"

@app.route("/")
def init():
    if 'gold' not in session:
        session['gold'] = 0

    if 'activities' not in session:
        session['activities'] = []
    return render_template("index.html", gold = session['gold'], results = session['activities'])

@app.route("/process_money", methods=["POST"])
def process():
    thisisdate = time.asctime(time.localtime(time.time()))
    if request.form['action'] == 'farm':
        number = random.randrange(10,21)
        session['gold'] += number
        session['activities'].append("Earned " + str(number) + " golds from the farm! " + thisisdate)
        return render_template("index.html", gold=session['gold'], results = session['activities'])
    elif request.form['action'] == 'cave':
        number = random.randrange(5, 11)
        session['gold'] += number
        session['activities'].append("Earned " + str(number) + " golds from the cave! " + thisisdate)
        return render_template("index.html", gold=session['gold'], results = session['activities'])
    elif request.form['action'] == 'house':
        number = random.randrange(2, 6)
        session['gold'] += number
        session['activities'].append("Earned " + str(number) + " golds from the house! " + thisisdate)
        return render_template("index.html", gold=session['gold'], results = session['activities'])
    else:
        number = random.randrange(2, 6)
        takeOrNot = random.randrange(0,2)
        if takeOrNot == 0:
            session['gold'] -= number
            session['activities'].append("Entered a casino and lost  " + str(number) + " golds... Ouch... " + thisisdate)
            return render_template("index.html", gold=session['gold'], results = session['activities'])
        else:
            session['gold'] += number
            session['activities'].append("Earned " + str(number) + " golds from the casino! " + thisisdate)
            return render_template("index.html", gold=session['gold'], results = session['activities'])


@app.route("/reset")
def reset():
    session['gold'] = 0
    session['activities'] = []
    return redirect("/")


app.run(debug=True)

