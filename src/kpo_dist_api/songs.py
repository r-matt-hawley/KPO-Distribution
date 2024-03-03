from flask import abort, make_response
from kpo_dist_api.config import db
from kpo_dist_api.models import Song, song_schema, songs_schema


def create(song):
    id = song.get("id")
    existing_song = Song.query.filter(Song.id == id).one_or_none()
    
    if existing_song is None:
        new_song = song_schema.load(song, session=db.session)
        db.session.add(new_song)
        db.session.commit()
        return song_schema.dump(new_song), 201
    else:
        abort(404, f"Song with id {id} already exists.")


def read_all():
    songs = Song.query.all()
    return songs_schema.dump(songs)


def read_one(id):
    song = Song.query.filter(Song.id == id).one_or_none()

    if song is not None:
        return song_schema.dump(song)
    else:
        abort(404, f"Song with id {id} not found.")


def update(id, song):
    existing_song = Song.query.filter(Song.id == id).one_or_none()

    if existing_song:
        update_song = song_schema.load(song, session=db.session)
        existing_song.title = update_song.title
        existing_song.concerts = update_song.concerts
        db.session.merge(existing_song)
        db.session.commit()
        return song_schema.dump(existing_song)
    else:
        abort(404, f"Song with id {id} not found.")


def delete(id):
    existing_song = Song.query.filter(Song.id == id).one_or_none()

    if existing_song:
        db.session.delete(existing_song)
        db.session.commit()
        return make_response(f"Song with id {id} successfully deleted.")
    else:
        abort(404, f"Song with id {id} not found.")
