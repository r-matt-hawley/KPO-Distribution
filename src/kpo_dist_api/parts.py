from flask import abort, make_response
from kpo_dist_api.config import db
from kpo_dist_api.models import Part, part_schema, parts_schema


def create(part):
    id = part.get("id")
    existing_part = Part.query.filter(Part.id == id).one_or_none()
    
    if existing_part is None:
        new_part = part_schema.load(part, session=db.session)
        db.session.add(new_part)
        db.session.commit()
        return part_schema.dump(new_part), 201
    else:
        abort(404, f"Part with id {id} already exists.")


def read_all():
    parts = Part.query.all()
    return parts_schema.dump(parts)


def read_one(part_id):
    part = Part.query.filter(Part.id == part_id).one_or_none()

    if part is not None:
        return part_schema.dump(part)
    else:
        abort(404, f"Part with id {part_id} not found.")


def update(part_id, part):
    existing_part = Part.query.filter(Part.id == part_id).one_or_none()

    if existing_part:
        update_part = part_schema.load(part, session=db.session)
        existing_part.part_name = update_part.part_name
        existing_part.songs = update_part.songs
        db.session.merge(existing_part)
        db.session.commit()
        return part_schema.dump(existing_part)
    else:
        abort(404, f"Part with id {part_id} not found.")


def delete(part_id):
    existing_part = Part.query.filter(Part.id == part_id).one_or_none()

    if existing_part:
        db.session.delete(existing_part)
        db.session.commit()
        return make_response(f"Part with id {part_id} successfully deleted.")
    else:
        abort(404, f"Part with id {part_id} not found.")
