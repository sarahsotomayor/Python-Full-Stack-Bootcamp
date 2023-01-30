from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import user_methods
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


#VISIBLE ROUTES
@app.route("/")
def index():
    return render_template('login_registration.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

#INVISIBLE/HIDDEN ROUTES
@app.route("/register", methods = ["POST"])
def register_user():
    if not user_methods.User.validate_user(request.form):
        print("Could Not Register")
        return redirect("/")
    user_methods.User.register_user(request.form)
    print("User Registered")
    data = { "email" : request.form["email"] }
    user_in_db = user_methods.User.get_by_email(data)
    session['user_name'] = user_in_db.first_name
    print("User in session")
    return redirect("/dashboard")

@app.route("/login", methods = ["POST"])
def login_user():
    data = { "email" : request.form["email"] }
    user_in_db = user_methods.User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect('/')
    session['user_name'] = user_in_db.first_name
    return redirect("/dashboard")

@app.route("/logout")
def logout_user():
    session.clear()
    print("User logged out")
    return redirect("/")
