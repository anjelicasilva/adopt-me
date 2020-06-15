from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class User(db.Model):
    """Store informtion about each user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique = True)
    password = db.Column(db.String(100), nullable=False)
    home_zipcode = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.now())

    favorites = db.relationship("Favorite")

    def __repr__(self):
        """Provide user's information in a helpful format"""
        return f"<User first_name={self.first_name}, last_name={self.last_name}, email={self.email}>"

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

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey("dogs.dog_id"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)

    user = db.relationship("User")
    dog = db.relationship("Dog")

    def __repr__(self): 
        
       return f"<Favorite dog_id={self.dog_id}, user_id={self.user_id}>" # Review for later

class Shelter(db.Model):
    """Store shelter information"""

    __tablename__ = "shelters"

    shelter_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    shelter_name = db.Column(db.String(30), nullable=True, unique = True)
    shelter_location_zipcode = db.Column(db.Integer, nullable=False)
    operation_hour = db.Column(db.String, nullable=False, default=datetime.today())


    def __repr__(self): 
        
        return f"<Shelter shelter_name={self.shelter_name}, shelter_location={self.shelter_location},\
                operation_hour={self.operation_hour}>"


class Dog(db.Model):
    """Store dog information in each shelter"""

    __tablename__ = "dogs"

    dog_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    shelter_id = db.Column(db.Integer, db.ForeignKey("shelters.shelter_id"))
    dog_breed = db.Column(db.String(30), nullable=False)
    dog_photo_url = db.Column(db.String(1000), nullable=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    fixed = db.Column(db.Boolean, nullable=False)

    shelter = db.relationship("Shelter", 
                                backref="dogs")
    favorites = db.relationship("Favorite")

    def __repr__(self): 

        return f"<Dog dog_breed={self.dog_breed}, dog_photo_url={self.dog_photo_url},\
                description={self.description}, gender={self.gender},\
                age={self.age}, fixed={self.fixed}>"


def connect_to_db(app, db_uri="postgresql:///adoptme_db"):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    db.create_all()
    print("Connected to DB.")

