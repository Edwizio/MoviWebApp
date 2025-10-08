from flask import Flask, request, render_template, url_for, redirect, flash
from pyexpat.errors import messages

from werkzeug.security import check_password_hash

from data_manager import DataManager
from models import db, Movie, User
import os


app = Flask(__name__)

# Using environment variables for secret_key
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-only')


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models

data_manager = DataManager() # Create an object of your DataManager class

# Creating Route and method to list users
@app.route('/')
def display_users():
    """This functions displays the list of users and a form to add new user"""
    users = data_manager.get_users()
    """for user in users:
        print(user.name)
        print(user.password)"""

    if not users:
        flash("Please add some users", "error")

        return render_template('index.html', users=users, messages=messages)

    return render_template('index.html', users=users)


# Creating route and method for adding new user
@app.route('/users',  methods=['GET','POST'])
def create_user():
    """This function add a new user to the database"""
    name = request.form.get("name")
    password = request.form.get("password")

    data_manager.create_user(name, password)

    flash("User added successfully", "success")
    return redirect(url_for('display_users'))


# Creating route and method to display user's list of favourite movies
@app.route('/users/<int:user_id>/movies', methods=['GET'])
def display_movies(user_id):
    """This function displays the favourite movies of the user based on ID"""
    # Extracting the user object to be used in jinja statements on webpage
    user = db.session.get(User, user_id)

    movies = data_manager.get_movies(user_id)
    return render_template('movies.html', movies=movies,user=user)


# Creating a route and method to add a new movie to the user's list
@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    """This method adds a movie to a user's list based on ID"""

    # Getting the title from the webpage
    movie = request.form.get('movie')
    user_year = request.form.get('year')  # Optional field

    # Error handling if movie title is not entered
    if not movie:
        flash("Please enter a movie name.", "error")
        return redirect(url_for('display_movies', user_id=user_id))

    success, message = data_manager.add_movie(movie, user_id, user_year)
    # Flash the message with category
    if success:
        flash(message, "success")
    else:
        flash(message, "error")

    # Extracting the user object to be used in jinja statements on webpage
    user = db.session.get(User, user_id)
    # and the list of the user's movies to be passed on as arguments to return statement
    movies = user.movies
    #flash("Movie Added to the database","success")
    return redirect(url_for('display_movies',user_id=user.id))


# Creating a route and method to modify the title of a specific movie in a user’s list
@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(movie_id, user_id):
    """This method updates the title of a movie based on it's ID"""

    # Extracting the user object to be used in jinja statements on webpage
    user = db.session.get(User, user_id)
    # and the list of the user's movies to be passed on as arguments to return statement
    movies = user.movies

    # Getting the new title from the webpage
    new_title = request.form.get('new_title')
    # Validating for empty string and whitespaces
    if not new_title.strip():
        flash("You have entered an empty string","error")
        return redirect(url_for('display_movies', user_id=user.id))

    data_manager.update_movie(movie_id, new_title)

    flash("Movie Title updated in the database", "success")
    return redirect(url_for('display_movies', user_id=user.id))


# Creating a route and method to remove a specific movie from a user’s favorite movie list
@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def remove_movie(movie_id, user_id):
    """This method removes a movie from a user's list"""

    # Extracting the user object to be used in jinja statements on webpage
    user = db.session.get(User, user_id)

    # and the list of the user's movies to be passed on as arguments to return statement
    movies = user.movies

    # Getting the password to check before deleting the movie
    password = request.form.get('password')
    if not check_password_hash(user.password, password):
        flash("Incorrect password. Movie not deleted.", "error")
        return redirect(url_for('display_movies', user_id=user.id))

    data_manager.delete_movie(movie_id)
    flash("Movie deleted successfully!", "success")
    return redirect(url_for('display_movies', user_id=user.id))


# Some common error handling routes defined to make code robust
@app.errorhandler(404)
def page_not_found(e):
    """Handles 404 error as the name dictates"""
    return render_template('404.html'), 404


@app.errorhandler(405)
def method_not_allowed(e):
    """Handles 405 error as the name dictates"""
    return render_template('405.html'), 405


@app.errorhandler(500)
def internal_server_error(e):
    """Handles 500 error as the name dictates"""
    return render_template('500.html'), 500


# Creating the database
if __name__ == '__main__':
    """with app.app_context():
        db.create_all()"""

    app.run(host='0.0.0.0', debug=True, port=5000)

