from flask_app import app
from flask import render_template, request, redirect, flash
from flask_app.models.user import User




@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def users():
    return render_template("all_users.html", all_users = User.get_all())

@app.route("/users/create")
def new_user_form():
    return render_template("create_user.html")

@app.route("/users/new", methods = ["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect("/")

@app.route("/users/<int:id>")
def show_user(id):
    return render_template('user.html', user=User.show_one_user({"id": id}))

@app.route("/users/<int:id>/edit")
def edit(id):
    return render_template("edit_user.html", user=User.show_one_user({"id": id}))

@app.route("/users/update", methods = ["POST"])
def edit_user():
    data = {
        'id' : request.form['id'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form ['last_name'],
        'email' : request.form['email']
    }
    User.update(data)
    return redirect (f"/users/{request.form['id']}")

@app.route("/users/<int:id>/delete")
def delete_user(id):
    User.delete_user({"id": id})
    return redirect ("/users")