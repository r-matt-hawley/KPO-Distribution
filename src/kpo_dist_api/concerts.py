from flask import abort, make_response, request
from kpo_dist_api.config import db, swagger, api
from kpo_dist_api.models import Concert, concert_schema, concerts_schema


from flask_restful import Resource

class ConcertsResource(Resource):
    @swagger.doc({
        "tags": ["Concerts"],
        "description": "Get a list of all concerts",
        "responses": {
            "200": {
                "description": "List of concerts",
                "schema": {"$ref": "#/definitions/Concert"}
            }
        }
    })
    def get(self):
        concerts = Concert.query.all()
        return concerts_schema.dump(concerts, many=True)

    @swagger.doc({
        "tags": ["Concerts"],
        "description": "Get one concert",
        "responses": {
            "200": {
                "description": "Return a single concert",
                "schema": {"$ref": "#/definitions/Concert"}
            }
        }
    })
    def get(self, concert_id):
        concert = Concert.query.get_or_404(concert_id)
        return concert_schema.dump(concert)

    @swagger.doc({
        "tags": ["Concerts"],
        "description": "Add a new Concert",
        "parameters": [
            {
                "name": "title",
                "in": "formData",
                "type": "string",
                "required": True,
                "description": "Title of the Concert"
            }
        ],
        "responses": {
            "201": {
                "description": "Concert added successfuly",
                "schema": {"$ref": "#/definitions/Concert"}
            }
        }
    })
    def post(self):
        title = request.form.get("title")
        new_concert = Concert(title=title)
        db.session.add(new_concert)
        db.session.commit()
        return concert_schema.dump(new_concert), 201
    

    @swagger.doc({
        "tags": ["Concerts"],
        "description": "Update an existing Concert",
        "parameters": [
            {
                "name": "id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "Id of the Concert to update"
            },
            {
                "name": "title",
                "in": "formData",
                "type": "string",
                "description": "New title for the concert"
            },
            {
                "name": "season",
                "in": "formData",
                "type": "string", # TODO: implement enum
                "description": "New season for the concert"
            }
        ],
        "responses": {
            "200": {
                "description": "Concert updated successfully",
                "schema": {"ref$": "#/definition/Concert"}
            },
            "404": {
                "description": "Concert not found"
            }
        }
    })
    def put(self, concert_id):
        concert = Concert.query.get_or_404(concert_id)
        new_title = request.form.get("title") | None
        new_season = request.form.get("season") | None

        if new_title is not None:
            concert.title = new_title

        if new_season is not None:
            concert.season = new_season
        
        db.session.merge(concert)
        db.session.commit()
        return concert_schema.dump(concert), 200

api.add_resource(ConcertsResource, '/concerts')





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


def read_one(concert_id):
    concert = Concert.query.filter(Concert.id == concert_id).one_or_none()

    if concert is not None:
        return concert_schema.dump(concert)
    else:
        abort(404, f"Concert with id {concert_id} not found.")


def update(concert_id, concert):
    existing_concert = Concert.query.filter(Concert.id == concert_id).one_or_none()

    if existing_concert:
        update_concert = concert_schema.load(concert, session=db.session)
        existing_concert.title = update_concert.title
        existing_concert.season = update_concert.season
        db.session.merge(existing_concert)
        db.session.commit()
        return concert_schema.dump(existing_concert)
    else:
        abort(404, f"Concert with id {concert_id} not found.")


def delete(concert_id):
    existing_concert = Concert.query.filter(Concert.id == concert_id).one_or_none()

    if existing_concert:
        db.session.delete(existing_concert)
        db.session.commit()
        return make_response(f"Concert with id {concert_id} successfully deleted.")
    else:
        abort(404, f"Concert with id {concert_id} not found.")
