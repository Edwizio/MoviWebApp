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