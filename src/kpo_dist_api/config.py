import pathlib
from connexion import FlaskApp
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os.path import join

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = FlaskApp(__name__, specification_dir=basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{join(basedir, 'db', 'music.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)