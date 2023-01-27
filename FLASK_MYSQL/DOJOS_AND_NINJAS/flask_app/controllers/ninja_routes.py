from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import ninja
from flask_app.models import dojo

#renders new ninja form
@app.route("/ninjas")
def ninjas():
    return render_template('new_ninja.html', all_dojos=dojo.Dojo.get_all_dojos())

#creates new ninja
@app.route("/ninjas/create", methods = ["POST"])
def save_ninja():
    ninja.Ninja.save_ninja(request.form)
    print("request.form", request.form)
    return redirect("/")

#deletes ninja
@app.route("/ninjas/delete/<int:id>")
def delete_ninja(id):
    dojo_id = session['dojo_id']
    ninja.Ninja.delete_ninja({"id": id})
    print("ninja deleted")
    return redirect (f"/dojos/{dojo_id}")

@app.route("/ninjas/edit/<int:id>")
def edit_ninja(id):
    data = {
        "id" : id
    }
    return render_template("edit_ninja.html", one_ninja = ninja.Ninja.get_one_ninja(data))

@app.route("/ninjas/update/<int:id>", methods = ["POST"])
def update(id):
    data = {
        "id" : id,
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    ninja.Ninja.update_ninja(data)
    print("request.form", request.form)
    return redirect (f"/dojos/{request.form['dojo_id']}")
