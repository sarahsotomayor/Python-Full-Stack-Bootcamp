from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import user_methods

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template('register_and_login.html')

@app.route("/register", methods = ["POST"])
def register_user():
    if not user_methods.User.validate_user(request.form):
        print("Could Not Register")
        return redirect("/")
    data = { 
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"]
     }
    session["user_id"] = user_methods.User.register_user(data)
    print("User Registered")
    print("User in session")
    return redirect("/recipes")

@app.route("/login", methods = ["POST"])
def login_user():
    data = { "email" : request.form["email"] }
    user_in_db = user_methods.User.get_one_user_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect('/')
    session['user_name'] = user_in_db.first_name
    session['user_id'] = user_in_db.id
    session['email'] = user_in_db.email
    print("User logged in")
    return redirect("/recipes")

@app.route("/logout")
def logout_user():
    if 'user_id' not in session:
        return redirect("/")
    session.clear()
    print("User logged out")
    return redirect("/")
