from flask import abort, make_response
from kpo_dist_api.config import db
from kpo_dist_api.models import Concert, concert_schema, concerts_schema


def create(concert):
    id = concert.get("id")
    existing_concert = Concert.query.filter(Concert.id == id).one_or_none()
    
    if existing_concert is None:
        new_concert = concert_schema.load(concert, session=db.session)
        db.session.add(new_concert)
        db.session.commit()
        return concert_schema.dump(new_concert), 201
    else:
        abort(404, f"Concert with id {id} already exists.")


def read_all():
    concerts = Concert.query.all()
    return concerts_schema.dump(concerts)


def read_one(id):
    concert = Concert.query.filter(Concert.id == id).one_or_none()

    if concert is not None:
        return concert_schema.dump(concert)
    else:
        abort(404, f"Concert with id {id} not found.")


def update(id, concert):
    existing_concert = Concert.query.filter(Concert.id == id).one_or_none()

    if existing_concert:
        update_concert = concert_schema.load(concert, session=db.session)
        existing_concert.title = update_concert.title
        existing_concert.season = update_concert.season
        db.session.merge(existing_concert)
        db.session.commit()
        return concert_schema.dump(existing_concert)
    else:
        abort(404, f"Concert with id {id} not found.")


def delete(id):
    existing_concert = Concert.query.filter(Concert.id == id).one_or_none()

    if existing_concert:
        db.session.delete(existing_concert)
        db.session.commit()
        return make_response(f"Concert with id {id} successfully deleted.")
    else:
        abort(404, f"Concert with id {id} not found.")
