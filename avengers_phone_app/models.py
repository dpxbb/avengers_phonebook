from avengers_phone_app import app, db, login_manager

# Import all of the Werkzeug Security methods
from werkzeug.security import generate_password_hash, check_password_hash

# Import for DateTime Module (This comes from python)
from datetime import datetime

# Import for the Login Manager UserMixin
from flask_login import UserMixin

@login_manager.user_loader
def load_user(hero_id):
    return User.query.get(int(hero_id))

# The User class will have 
# An id, heroname, email, 
# password, phonenumber, 

@login_manager.user_loader
def load_user(hero_id): 
    return User.query.get(int(hero_id))

# now creating a SQL table class hero
class Hero(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique = True)
    phone = db.Column(db.String(20), unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.column(db.String(256))

    def __init__(self, name, phone, email, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = self.set_password(password)

    def set_password(password):
        """
            Grab the password that is pased into the method
            return the hashed version of the password
            which will be stored inside the database
        """
        return generate_password_hash(password)

    def __repr__(self):
        return f"{self.name}'s phonebook entry has created with the phone, number: {self.phone} and the email: {self.email}."