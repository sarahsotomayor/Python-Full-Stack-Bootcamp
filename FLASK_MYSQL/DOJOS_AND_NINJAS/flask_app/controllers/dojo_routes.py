from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo

#renders all dojos
@app.route("/")
def index():
    return redirect("/dojos")

#renders all dojos
@app.route("/dojos")
def dojos():
    return render_template('view_all_dojos.html', all_dojos=Dojo.get_all_dojos())

#creates new dojo from view_all_dojos.html New Dojo section
@app.route("/dojos/create", methods = ["POST"])
def save_dojo():
    print("request.form", request.form)
    Dojo.save_dojo(request.form)
    return redirect("/dojos")

#renders one dojo with its ninjas
@app.route("/dojos/<int:id>")
def view_one_dojo(id):
    session['dojo_id'] = id
    return render_template('view_one_dojo.html', dojo=Dojo.get_dojo_with_ninjas({"id": id}))