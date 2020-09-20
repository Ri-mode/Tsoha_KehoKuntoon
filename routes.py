from app import app
#import visits
from flask import render_template, request

@app.route("/")
def index():
#    visits.add_visit()
#    counter = visits.get_counter()
    return render_template("index.html")
    #, counter=counter)

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html",name=request.index["name"], weight=request.index["weight"])