from flask_app.config.Mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user_methods

db = "users_and_recipes"

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.cook_time = data['cook_time']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def validate_recipe(self, data):
        is_valid = True
        if len(data['name']) < 3:
            is_valid = False
            flash("Name cannot be less than 3 characters", "recipe")
        if len(data['description']) < 4:
            is_valid = False
            flash("Description must be at least 4 characters", "recipe")
        if len(data['instructions']) < 10:
            is_valid = False
            flash("Instructions must be at least 10 characters", "recipe")
        return is_valid

    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, cook_time, instructions, date_cooked, user_id) VALUES (%(name)s, %(description)s, %(cook_time)s, %(instructions)s, %(date_cooked)s, %(user_id)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, user_id=%(user_id)s WHERE id=%(id)s ;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s;" 
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_recipes_with_users(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(db).query_db(query)
        print(results)
        if len(results) == 0:
            return []
        else:
            all_recipe_objects = []
            for recipe_dictionary in results:
                recipe_object = cls(recipe_dictionary)
                user_dictionary = {
                    "id" : recipe_dictionary['users.id'],
                    "first_name" : recipe_dictionary['first_name'],
                    "last_name" : recipe_dictionary['last_name'],
                    "email" : recipe_dictionary['email'],
                    "password" : recipe_dictionary['password'],
                    "created_at" : recipe_dictionary['users.created_at'],
                    "updated_at" : recipe_dictionary['users.updated_at']
                }
                user_object = user_methods.User(user_dictionary)
                recipe_object.user = user_object
                all_recipe_objects.append(recipe_object)
        return all_recipe_objects

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id=%(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        recipe_object = cls(results[0])
        user_dictionary = {
                    "id" : results[0]['users.id'],
                    "first_name" : results[0]['first_name'],
                    "last_name" : results[0]['last_name'],
                    "email" : results[0]['email'],
                    "password" : results[0]['password'],
                    "created_at" : results[0]['users.created_at'],
                    "updated_at" : results[0]['users.updated_at']
                }
        user_object = user_methods.User(user_dictionary)
        recipe_object.user = user_object
        return recipe_object
