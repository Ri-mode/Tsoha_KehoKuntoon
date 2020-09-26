from app import app
from db import db
from flask import redirect, render_template, request
import users

@app.route("/")
def index():
#    visits.add_visit()
#    counter = visits.get_counter()
    return render_template("index.html")
    #, counter=counter)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
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
        if users.register_normal(username,password):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti epäonnistui!")



@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html")#,name=request.index["name"], weight=request.index["weight"])