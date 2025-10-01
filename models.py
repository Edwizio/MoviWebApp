from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Defining the User model as a class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Adding the relationship to Book class
    movies = db.relationship("Movie", backref="user", lazy=True)

    def __repr__(self):
        return f"User(id = {self.id}, name = {self.name})"

    def __str__(self):
        return f"The id {self.id} represents the user {self.name}"

# Defining the Movie model as a class
class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String (200), nullable=False)
  director = db.Column(db.String (200), nullable=False)
  year = db.Column(db.Integer, nullable=False)
  poster_url = db.Column(db.String (500), nullable=False)

  # Link Movie to User
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
      return f"Movie (id = {self.id}, name = {self.name})"

  def __str__(self):
      return f"The id {self.id} represents the movie {self.name}"