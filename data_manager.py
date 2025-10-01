from models import db, User, Movie
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

class DataManager():
    # Define Crud operations as methods
    def create_user(self, name):
        """This method creates a new user"""
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_users(self):
        """This function returns a list of the existing users"""
        users = User.query.all()
        return users

    def get_movies(self, user_id):
        """This function returns a list of all movies of a specific user"""
        movies = Movie.query.join(User).order_by(user_id).all()
        return movies

    def add_movie(self, movie):
        api_url = f"https://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
        response = requests.get(api_url)

        # Error Handling if website isn't accessible
        if response.status_code == requests.codes.ok:
            movie_data = response.json()

            # Creating new Movie object
            new_movie = Movie(
                name = movie_data['Title'],
                director = movie_data['Director'],
                year = int(movie_data['Year']),
                poster_url = movie_data['Poster']

            )

            db.session.add(new_movie)
            db.session.commit()

    def update_movie(self, movie_id, new_title):
        """This function updates the movie title using the movie ID"""

        # Fetching the correct Movie Object
        movie = Movie.query.get(movie_id)

        # Updating the title
        movie.name = new_title
        db.session.commit()


    def delete_movie(self, movie_id):
        """This function deletes a movie based on it's ID"""

        # Fetching the correct Movie Object
        movie = Movie.query.get(movie_id)

        # Deleting the movie from the database
        db.session.delete(movie)
        db.session.commit()

