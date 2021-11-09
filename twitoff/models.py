"""SQLAlchemy User and Tweet models for our database"""
from flask_sqlalchemy import SQLAlchemy

# creates a DB Object from SQLAlchemy class
DB = SQLAlchemy()

# Making a User table using SQLAlchemy
# SQLAlchemy lets us use Python Classes to set up the DB schema
class User(DB.Model):
    """Creates a User Table with SQlAlchemy"""
    # The ID column will be our Primary Key
    id = DB.Column(DB.BigInteger, primary_key=True)
    # Each user will just have a name for now
    username = DB.Column(DB.String, nullable=False)

    # This function changes how class objects are represented as strings. 
    def __repr__(self):
        return "<User: {}>".format(self.username)


class Tweet(DB.Model):
    """Keeps track of Tweets for each user"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))  # allows for text and links
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
        'user.id'), nullable=False)
    #Eestablish a collection of tweet objects on the 'User'name model. 
    # A user can now be associated with multiple tweets.
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)