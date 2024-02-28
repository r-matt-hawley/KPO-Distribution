from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import Mapped

from kpo_dist_api.config import db, ma


def make_created_column():
    return db.mapped_column(db.DateTime, default=datetime.utcnow)


def make_modified_column():
    return db.mapped_column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Association Tables for many-to-many relationships

concert_song = db.Table('concert_song',
                        db.Column('concert_id', db.Integer, db.ForeignKey('concert.id')),
                        db.Column('song_id', db.Integer, db.ForeignKey('song.id'))
                        )

# SQLAlchemy Models that map Python objects to SQL commands

class Concert(db.Model):
    # TODO: Can title be the primary_key?
    __tablename__ = "concert"
    id = db.mapped_column(db.Integer, primary_key=True)
    title = db.mapped_column(db.String(32), unique=True)
    season = db.mapped_column(db.String(15)) # Eventually int for enum
    songs: Mapped[list[Song]] = db.relationship(
        secondary=concert_song,
        back_populates="concerts"
    )
    created = make_created_column()
    modified = make_modified_column()

    def __repr__(self):
        return f'<Concert "{self.title}">'

class Song (db.Model):
    # TODO: Add composer and arranger as primary_keys
    __tablename__= "song"
    id = db.mapped_column(db.Integer, primary_key=True)
    title = db.mapped_column(db.String(32), unique=True)
    concerts: Mapped[list[Concert]] = db.relationship(
        secondary=concert_song, 
        back_populates='songs')
    created = make_created_column
    modified = make_modified_column

    def __repr__(self):
        return f'<Song "{self.title}">'
    

    def __eq__(self, other):
        print("-"*10, "\nSong.__eq__ accessed\n", "-"*10)
        return isinstance(other, Song) and self.title == other.title
    
    def __contains__(self, item):
        print("-"*10, "\nSong.__contains__ accessed\n", "-"*10)
        return item == self.title

# Marshmallow schemas that (de)serialize data to/from the db

class ConcertSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Concert
        load_instance = True
        sqla_session = db.session

class SongSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Song
        load_instance = True
        sqla_session = db.session

# Expose schemas to the other api files
concert_schema = ConcertSchema() # read_one, e.g.
concerts_schema = ConcertSchema(many=True) # read_all
song_schema = SongSchema()
songs_schema = SongSchema(many=True)