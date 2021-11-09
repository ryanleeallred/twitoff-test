from re import DEBUG
from flask import Flask, render_template
from .models import DB, User, Tweet

def create_app():

    # Initilaize our app
    app = Flask(__name__)

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    # Create a new "route" that detects when a user accesses it.
    # We'll attatch each route to our `app` object.
    @app.route('/')
    def root():
        # return page contents
        users = User.query.all()
        return render_template('base.html', title="Home", users=users)

    app_title = "Twitoff DS32"

    @app.route("/test")
    def test():
        return f"<p>Another {app_title} page</p>"

    @app.route('/hola')
    def hola():
        return "hola, Twitoff"

    @app.route('/salut')
    def salut():
        return "salut, Twitoff"

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return '''The database has been reset. 
        <a href='/'>Go to Home</a>
        <a href='/reset'>Go to reset</a>
        <a href='/populate'>Go to populate</a>'''

    @app.route('/populate')
    def populate():
        ryan = User(id=1, username='ryan')
        DB.session.add(ryan)
        julian = User(id=2, username='julian')
        DB.session.add(julian)
        tweet1 = Tweet(id=1, text='tweet text', user=ryan)
        DB.session.add(tweet1)
        DB.session.commit()
        return '''Created some users. 
        <a href='/'>Go to Home</a>
        <a href='/reset'>Go to reset</a>
        <a href='/populate'>Go to populate</a>'''

    # return our app object after attaching the routes to it.
    return app 