from flask import request

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
        return new_user

    def get_users(self):
        """This function returns a list of the existing users"""
        users = User.query.all()
        return users

    def get_movies(self, user_id):
        """This function returns a list of all movies of a specific user"""
        user = User.query.get(user_id)
        if not user:
            return [] # error handling
        return user.movies

    def add_movie(self, movie, user_id, user_year=None):
        """This method takes a movie a parameter and an optional year parameter, retrieves
        the relevant info from OMDBAPI and adds to a user's list of favourites"""

        api_url = f"https://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
        response = requests.get(api_url)

        # Error Handling if website isn't accessible
        if response.status_code == requests.codes.ok:
            movie_data = response.json()

            if movie_data.get("Response") == "False":
                return False, f"Movie not found: {movie_data.get('Error')}"

            else:
                # Use user-provided year if given, else fetch from OMDB
                year = user_year if user_year else movie_data.get("Year") or 0

                # If poster is not available on the OMBD, replace with placholder image
                poster_url = movie_data.get("Poster")
                if not poster_url or poster_url == "N/A":
                    poster_url = "/static/images/placeholder.png"

                # Creating new Movie object
                new_movie = Movie(
                    name=movie_data.get("Title") or "Unknown",
                    director=movie_data.get("Director") or "Unknown",
                    year=year,
                    poster_url=poster_url,
                    user_id=user_id

                )

            db.session.add(new_movie)
            db.session.commit()
            return True, f"Movie '{movie}' added successfully!"
        else:
            return False, f"Error : {response.status_code, response.text}"


    def update_movie(self, movie_id, new_title):
        """This function updates the movie title using the movie ID"""

        # Fetching the correct Movie Object
        movie = Movie.query.get(movie_id)

        # Updating the title
        movie.name = new_title
        db.session.commit()
        return movie


    def delete_movie(self, movie_id):
        """This function deletes a movie based on it's ID"""

        # Fetching the correct Movie Object
        movie = Movie.query.get(movie_id)

        # Deleting the movie from the database
        db.session.delete(movie)
        db.session.commit()
        return movie

