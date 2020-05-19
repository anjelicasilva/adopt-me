from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime, date
from wekzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class User(db.Model):
    """Store informtion about each user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey("favorites.favorite_id"))
    email = db.Column(db.String(30), nullable=True, unique = True)
    password = db.Column(db.String(100), nullable=True)
    home_location = db.Column(db.String(100), nullable=False)

    favorites = db.relationship("Favorite",
                                backref="users")

    def __repr__(self):
        """Provide user's information in a helpful format"""
        return f"User("{self.first_name}", "{self.last_name}", "{self.email}")"

    def to_dict(self):
        return {"user_id": self.user_id,
                "email": self.email,
                "password": self.password,
                "home_location": self.home_location
                }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Favorite(db.Model):
    """Store favorite pets for each user"""

    ___tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dogs_id_list = db.Column()

    def __repr__(self): 
        
       return f"User("{self.dogs_id_list}")"

class Shelter(db.Model):
    """Store shelter information"""

    ___tablename__ = "shelters"

    shelter_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    shelter_name = db.Column(db.String(30), nullable=True, unique = True)
    shelter_location = db.Column(db.String(100), nullable=False)
    operation_hour = db.Column(db.String, nullable=False, default=datetime.today())

    def __repr__(self): 
        
        return f"Shelter("{self.shelter_name}", "{self.shelter_location}", \
                "{self.operation_hour}")"


class DOG(db.Model):
    """Store dog information in each shelter"""

    __tablename__ = "dogs"

    dog_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    shelter_id = db.Column(db.Integer, db.ForeignKey("shelters.shelter_id"))
    dob_breed = db.Column(db.String(30), nullable=True, unique = True)
    dog_photo_url = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    gender = db.Column(db.String(30), nullable=True, unique = True)
    age = db.Column(db.Integer, nullable=True)
    fixed = db.Column(db.String(30), nullable=True, unique = True)

    shelters = db.relationship("Shelter", backref="dogs")

    def __repr__(self): 

        return f"DOG("{self.dog_breed}", "{self.dog_photo_url}", \
                "{self.description}", "{self.gender}", "{self.gender}", \
                "{self.age}", "{self.fixed}")"
















def connect_to_db(app, db_uri="postgresql:///adoptme_db"):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    print("Connected to DB.")

