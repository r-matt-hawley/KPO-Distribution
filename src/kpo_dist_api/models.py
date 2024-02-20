from datetime import datetime
from kpo_dist_api.config import db, ma

# SQLAlchemy Models that map Python objects to SQL commands

class Concert(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), unique=True)
    season = db.Column(db.String(10)) # Eventually int for enum
    created = db.Column(db.DateTime, default=datetime.utcnow)
    modified = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

# Marshmallow schemas that (de)serialize data to/from the db

class ConcertSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Concert
        load_instance = True
        sqla_session = db.session

# Expose schemas to the other api files
concert_schema = ConcertSchema() # read_one, e.g.
concerts_schema = ConcertSchema(many=True) # read_all