from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import recipe_methods, user_methods

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route("/recipes/new")
def create_recipe():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("add_recipe.html")

@app.route("/recipes/create", methods = ["POST"])
def create_recipe_process():
    if 'user_id' not in session:
        return redirect("/")
    if not recipe_methods.Recipe.validate_recipe(request.form):
        print("Could Not Save Recipe")
        return redirect("/recipes/new")
    data={
        "user_id" : session['user_id'],
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "date_cooked" : request.form['date_cooked'],
        "cook_time" : request.form['cook_time'],
    }
    recipe_methods.Recipe.add_recipe(data)
    print("Recipe Saved", "request.form", request.form)
    return redirect("/recipes")

@app.route("/recipes")
def get_all_recipes():
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "id" : session['user_id'],
    }
    return render_template('recipes.html', all_recipes = recipe_methods.Recipe.get_all_recipes_with_users(), current_user = user_methods.User.get_one_user_by_email(data))

@app.route("/recipes/<int:id>")
def view_recipe(id):
    if 'user_id' not in session:
        return redirect("/")
    session['recipe_id'] = id
    data = {
        "id" : id
    }
    return render_template("view_recipe.html", recipe = recipe_methods.Recipe.get_one_recipe(data))

@app.route("/recipes/edit/<int:id>")
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "id" : id
    }
    return render_template("edit_recipe.html", recipe = recipe_methods.Recipe.get_one_recipe(data))

@app.route("/recipes/update/<int:id>", methods = ["POST"])
def edit_recipe_process(id):
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "id" : id,
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "user_id" : request.form['user_id']
    }
    recipe_methods.Recipe.edit_recipe(data)
    print("request.form", request.form)
    return redirect ("/recipes")

@app.route("/recipes/delete/<int:id>")
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect("/")
    recipe_methods.Recipe.delete_recipe({"id": id})
    print("recipe deleted")
    return redirect ("/recipes")
