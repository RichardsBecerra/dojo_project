from misgastos_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__ (self, data):
        self.uid = data['uid']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']

    @classmethod
    def get(cls, data):
        if 'email' in data:
            query = 'select * from users where email = %(email)s'
        if 'uid' in data:
            query = 'select * from users where uid = %(uid)s'
        result = connectToMySQL('dojo_project').query_db(query, data)
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = 'select * from users order by last_name asc;'
        results = connectToMySQL('dojo_project').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = 'insert into users (first_name, last_name, email, password, created_at) values (%(first_name)s, %(last_name)s, %(email)s, %(password)s, now());'
        return connectToMySQL('dojo_project').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'update users set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = now() where uid = %(uid)s;'
        return connectToMySQL('dojo_project').query_db(query, data)

    @staticmethod
    def validate_data(data):
        is_valid = True

        if len (data['first_name']) < 3:
            flash('Nombre debe tener min 3 letras')
            is_valid = False
        
        if len (data['last_name']) < 3:
            flash('Apellido debe tener min 3 letras')
            is_valid = False
        
        if not EMAIL_REGEX.match(data['email']): 
            flash("La dirección de email debe ser valida, ej. alice@gmail.com")
            is_valid = False
        try:
            if len (data['password']) < 8:
                flash('Password debe tener min 8 letras y números')
                is_valid = False
            
            if re.search ('[0-9]', data['password']) is None:
                flash('Password debe tener min 1 número')
                is_valid = False
            
            if re.search ('[a-z]', data['password']) is None:
                flash('Password debe tener min 1 letra minúscula')
                is_valid = False

            if re.search ('[A-Z]', data['password']) is None:
                flash('Password debe tener min 1 letra mayúscula')
                is_valid = False
            
            if data['password'] != data['confirm_password']:
                flash("Password diferentes")
                is_valid = False
        except:
            pass
        return is_valid