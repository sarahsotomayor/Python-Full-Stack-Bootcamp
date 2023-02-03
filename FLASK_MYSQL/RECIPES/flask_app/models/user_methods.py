from flask_app.config.Mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
from flask_app.models import recipe_methods

bcrypt = Bcrypt(app)

db = "users_and_recipes"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data["first_name"]) < 2:
            is_valid = False
            flash("First name must be 2 or more characters", "register")
        if len(data["last_name"]) < 2:
            is_valid = False
            flash("Last name must be 2 or more characters", "register")
        if not EMAIL_REGEX.match(data['email']): 
            flash("Email is not in correct format", "register")
            is_valid = False
        if len(data["password"]) < 8:
            is_valid = False
            flash("Password must be 8 or more characters", "register")
        if data["password"] != data["confirm_password"]:
            is_valid = False
            flash("Passwords must match", "register")
        return is_valid

    @classmethod
    def register_user(cls, data):
        pw_hash = bcrypt.generate_password_hash(data["password"])
        data = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "email": data["email"],
            "password": pw_hash
        }
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_one_user_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query,data)
        if not result:
            return None
        return cls(result[0])