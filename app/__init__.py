from flask import Flask
from app.configs import database, migrations
from dotenv import load_dotenv
from os import getenv
from app import routes


def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    database.init_app(app)
    migrations.init_app(app)

    routes.init_app(app)
    return app
