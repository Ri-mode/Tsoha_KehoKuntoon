from app import app
from db import db
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
        if users.register_normal(username, password, current_weight, target_weight, height):
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
        weight_now = request.form["weight"]
        fat_now = request.form["fat"]
        mustcle_now = request.form["muscle"]
        
        if weights.add_weight(users.user_id(), weight_now, fat_now, mustcle_now):
            return redirect("/")
        else:
            return render_template("error.html", message="Tietojen lisäys epäonnistui!")

@app.route("/result", methods=["GET"])
def result():
    print(users.user_id())
    list = weights.get_weights(users.user_id())
    print(list)
    return render_template("result.html", messages=list)
