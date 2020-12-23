from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50), unique=True)

    def to_json(self):
        return {'id': self.id, 'name': self.name}


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(150), unique=True)
    year = db.Column(db.Integer, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))

    genre = db.relationship("Genre")

    def to_json(self):
        return {'id': self.id, 'title': self.title,
                'year': self.year,
                'genre': dict(id=self.genre.id, name=self.genre.name)}
