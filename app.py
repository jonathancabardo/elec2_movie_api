import os
from flask import Flask
from resources import api
from models import db

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
api.init_app(app)
db.init_app(app)

# db configuration
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///" + os.path.join(base_dir, "db.sqlite")

if __name__ == "__main__":
    app.run(debug=True)
