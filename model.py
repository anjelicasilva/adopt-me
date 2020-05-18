from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(30), nullable=True, unique = True)
    password = db.Column(db.String(100), nullable=True)
    home_location = db.Column(db.String(100), nullable=False)


    companies = db.relationship("Company",
                                backref="users",
                                secondary="user_companies")

    def __repr__(self):
        """Provide user's information in a helpful format"""

        return f"<User user_id={self.user_id}>"


class FAVORITE(db.Model):

    ___tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dogs_id_list = 

class SHELTER(db.Model):

    ___tablename__ = "shelters"

    shelter_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    shelter_name = db.Column(db.String(30), nullable=True, unique = True)
    shelter_location = db.Column(db.String(100), nullable=False)
    hours = db.Column(db.String(100), nullable=False)

class DOG(db.Model):

    __tablename__ = "dogs"

    dog_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dob_breed = db.Column(db.String(30), nullable=True, unique = True)
    dog_photo = db.Column(db.String(30), nullable=True, unique = True)
    description = db.Column(db.String(200), nullable=True)
    gender = db.Column(db.String(30), nullable=True, unique = True)
    age = db.Column(db.Integer, nullable=True)
    fixed = db.Column(db.String(30), nullable=True, unique = True)
    



















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

