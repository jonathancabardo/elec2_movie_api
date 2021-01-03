from flask_restx import Namespace, Resource, Api
from flask import request

from models import Genre, Movie, db

api_genre = Namespace("genres")
api_movie = Namespace("movies")

api = Api()
api.add_namespace(api_genre)
api.add_namespace(api_movie)


# /genres
@api_genre.route("")
class GenreList(Resource):
    def get(self):
        """Return all genres"""
        genres = Genre.query.all()
        return {"genres": [genre.to_json() for genre in genres]}

    def post(self):
        """Create new genre"""
        # 1. get request body
        data = request.get_json()
        # 2. create genre instance/object
        genre = Genre(name=data['name'])
        # 3. add genre instance/object to db transaction
        db.session.add(genre)
        # 4. commit transaction
        db.session.commit()
        # 5. return genre as response with 201 response code
        return {"genre": genre.to_json()}, 201


# /genres/<int:genre_id>
@api_genre.route("/<int:genre_id>")
class GenreById(Resource):
    def get(self, genre_id):
        """Return a genre"""
        genre = Genre.query.get(genre_id)
        if genre is None:
            # return 404
            return {"message": "The given genre ID does not exist."}, 404
        return {"genre": genre.to_json()}

    def put(self, genre_id):
        """Update a genre"""
        # get request body
        data = request.get_json()
        # 1. Find genre by id, return 404 if not found
        genre = Genre.query.get(genre_id)
        if genre is None:
            return {"message": "The given genre ID does not exist."}, 404
        # 2. Update genre
        genre.name = data["name"]
        # add genre to session/transaction & commit
        db.session.add(genre)
        db.session.commit()
        # 3. return genre
        return {"genre": genre.to_json()}, 200


# /movies
@api_movie.route("")
class MovieList(Resource):
    def get(self):
        """Return all movies"""
        movies = Movie.query.all()
        return {"movies": [movie.to_json() for movie in movies]}

    def post(self):
        """Create new movie"""
        data = request.get_json()
        # 1. validate genre, return 404 if invalid
        genre = Genre.query.get(data["genre"])
        if genre is None:
            # return 404
            return {"message": "The given genre ID does not exist."}, 404
        # 2. create new movie instance
        movie = Movie()
        movie.title = data["title"]
        movie.year = data["year"]
        # movie.genre_id = data["genre"]
        movie.genre = genre
        # 3. add instance to session, and commit
        db.session.add(movie)
        db.session.commit()
        # 4. return new created movie
        return {"movie": movie.to_json()}, 201


# /movies/id
@api_movie.route("/<int:movie_id>")
class MovieById(Resource):
    def get(self, movie_id):
        """Return a movie"""
        # ----- YOUR CODE HERE ----
        return {}

    def put(self, movie_id):
        """Update a movie"""
        # ----- YOUR CODE HERE ------
        # 1. find movie, return 404 if not found
        # 2. Validate genre, return 404 if invalid
        # 3. Update movie (title, year, genre)
        # add movie to session, and commit
        # 4. return updated movie
        return {}
