from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Defining the User model as a class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Adding the Python side relationship to Movie class to connect the two classes in both directions, without this,
    # the database will still work but only half of the links exist
    movies = db.relationship("Movie", back_populates="user", cascade="all, delete-orphan")

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
  user = db.relationship("User", back_populates="movies")
  def __repr__(self):
      return f"Movie (id = {self.id}, name = {self.name})"

  def __str__(self):
      return f"The id {self.id} represents the movie {self.name}"