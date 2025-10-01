from flask import Flask, request
from data_manager import DataManager
from models import db, Movie
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models

data_manager = DataManager() # Create an object of your DataManager class

# Creating Route and method to list users
@app.route('/')
def list_users():
    """This functions displays the list of users and a form to add new user"""
    users = data_manager.get_users()
    return str(users)  # Temporarily returning users as a string


# Creating route and method for adding new user
@app.route('/users',  methods=['POST'])
def add_user(name):
    """This function add a new user to the database"""
    data_manager.create_user(name)


# Creating route and method to display user's list of favourite movies
@app.route('/users/<int:user_id>/movies', methods=['GET'])
def display_movies(user_id):
    """This function displays the favourite movies of the user based on ID"""
    data_manager.get_movies(user_id)


# Creating a route and method to add a new movie to the user's list
@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    """This method adds a movie to a user's list based on ID"""
    # Getting the title from the webpage
    movie = request.form.get('movie')

    data_manager.add_movie(movie)


# Creating a route and method to modify the title of a specific movie in a user’s list
@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(movie_id, new_title):
    """This method updates the title of a movie based on it's ID"""
    # Getting the new title from the webpage
    new_title = request.form.get('new_title')

    data_manager.update_movie(movie_id, new_title)


# Creating a route and method to remove a specific movie from a user’s favorite movie list
@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def remove_movie(movie_id):
    """This method removes a movie from a user's list"""

    data_manager.delete_movie(movie_id)


# Creating the database
if __name__ == '__main__':
    """  with app.app_context():
    db.create_all()"""

    app.run()

