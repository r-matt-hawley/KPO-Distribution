from datetime import datetime

from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


CONCERTS = {
    1: {
        "id": 1,
        "season": "Spring 2023",
        "title": "Ticket to Ride",
        "created": get_timestamp(),
        "modified": get_timestamp(),
    },
    2: {
        "id": 2,
        "season": "Fall 2023",
        "title": "Liberty Belles",
        "created": get_timestamp(),
        "modified": get_timestamp(),
    },
    3: {
        "id": 3,
        "season": "Christmas 2023",
        "title": "Christmas at the Movies",
        "created": get_timestamp(),
        "modified": get_timestamp(),
    },
    4: {
        "id": 4,
        "season": "March 2024",
        "title": "Tribute to John Williams",
        "created": get_timestamp(),
        "modified": get_timestamp(),
    },
}


def create(concert):
    id = concert.get("id")
    title = concert.get("title")
    season = concert.get("season")

    if id and id not in CONCERTS:
        CONCERTS[id] = {
            "id": id,
            "title": title,
            "season": season,
            "created": get_timestamp(),
        }
        return CONCERTS[id], 201
    else:
        abort(404, f"Concert with id {id} already exists.")


def read_all():
    return list(CONCERTS.values())


def read_one(id):
    if id in CONCERTS:
        return CONCERTS[id]
    else:
        abort(404, f"Concert with id {id} not found.")


def update(id, concert):
    if id in CONCERTS:
        CONCERTS[id]["title"] = concert.get("title", CONCERTS[id]["title"])
        CONCERTS[id]["season"] = concert.get("season", CONCERTS[id]["season"])
        CONCERTS[id]["modified"] = get_timestamp()
        return CONCERTS[id]
    else:
        abort(404, f"Concert with id {id} not found.")


def delete(id):
    if id in CONCERTS:
        del CONCERTS[id]
        return make_response(f"Concert with id {id} successfully deleted.", 200)
    else:
        abort(404, f"Concert with id {id} not found.")
