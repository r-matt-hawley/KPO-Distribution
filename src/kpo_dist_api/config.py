import pathlib
from os.path import join

from flasgger import Swagger
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# from kpo_dist_api.concerts import ConcertsResource

basedir = pathlib.Path(__file__).parent.resolve()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{join(basedir, 'db', 'music.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SWAGGER"] = {
    "title": "KPO Music Distribution REST API",
    "uiversion": 3,
}


db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
swagger = Swagger(app)

# api.add_resource(ConcertsResource)