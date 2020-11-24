import secrets
from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app)


# in-memory database
# id, title, year, genre (name, id)
movies = []
genres = [
    {
      "name": "Comedy",
      "id": "e04197a460e77393"
    },
    {
      "name": "Horror",
      "id": "b0085d9f782ed5fb"
    },
    {
      "name": "Action",
      "id": "e105fb2b1c85e34d"
    }
  ]


# decoratora
@api.route('/genres')
class GenreList(Resource):
    # Get all genre
    def get(self):
        return {"genres": genres}, 200

    # Create genre
    def post(self):
        _id = secrets.token_hex(8)
        data = request.get_json()
        data.update({"id": _id})
        genres.append(data)
        return data, 201


@api.route('/genres/<string:id>')
class GenreById(Resource):
    # Get genre by id
    def get(self, id):
        for genre in genres:
            if genre['id'] == id.strip():
                return genre, 200
        return {"message": "Genre ID not found"}, 404

    # Update genre
    def put(self, id):
        data = request.get_json()
        for genre in genres:
            if genre['id'] == id.strip():
                genre["name"] = data["name"]
                return genre, 200
        return {"message": "Genre ID not found"}, 404
    
    # Delete genre
    def delete(self, id):
        data = request.get_json()
        for idx, genre in enumerate(genres):
            if genre['id'] == id.strip():
                genres.pop(idx)
                return {"message": "Genre deleted"}, 200
        return {"message": "Genre ID not found"}, 404


@api.route('/movies')
class MovieList(Resource):
    # get, post
    pass

if __name__ == '__main__':
    app.run(debug=True)

# SQLite (file based)