from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo




class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        self.dojos = []

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id=%(id)s;" 
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas=[]
        print(results)
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def update_ninja(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, dojo_id=%(dojo_id)s WHERE id=%(id)s ;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(results[0])


