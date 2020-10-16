from app import app
from db import db
from datetime import date
from flask import redirect, render_template, request, session
import users, weights

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print("user:", username)
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html", message="Käyttäjätunnus tai salasana virheellinen!")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        current_weight = request.form["currentweight"]
        target_weight = request.form["targetweight"]
        height = request.form["height"]
        if len(username) > 25 or len(password) > 25:
            return render_template("error.html", message="Käyttäjätunnus tai salasana on yli 25 merkkiä pitkä")
        if users.register_normal(username, password, target_weight, height):
            weights.add_weight(users.user_id(), current_weight, date.today())
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti epäonnistui!")

@app.route("/register_coach", methods=["GET", "POST"])
def register_coach():
    if request.method == "GET":
        return render_template("register_coach.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if len(username) > 25 or len(password) > 25:
            return render_template("error.html", message="Käyttäjätunnus tai salasana on yli 25 merkkiä pitkä")
        if users.register_coach(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti epäonnistui!")

@app.route("/weight", methods=["GET", "POST"])
def weight():
    if request.method == "GET":
        return render_template("weight.html")
    if request.method == "POST":
        date_now = request.form["inputdate"]
        weight_now = request.form["weight"]
        if date_now == '':
            date_now = date.today()
        else:
            date_now = date(int(date_now[0:4]), int(date_now[5:7]), int(date_now[8:]))
        if date_now > date.today():
            return render_template("error.html", message="Et voi lisätä merkintää tulevaisuuteen!")
        if weights.check_date(users.user_id(), date_now):
            return render_template("error.html", message="Antamallesi päivälle on jo merkintä!")
        if weights.add_weight(users.user_id(), weight_now, date_now):
            return redirect("/")
        else:
            return render_template("error.html", message="Tietojen lisäys epäonnistui!")

@app.route("/result", methods=["GET"])
def result():
    list = weights.get_weights(users.user_id())
    return render_template("result.html", messages=list)
