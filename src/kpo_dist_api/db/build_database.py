from kpo_dist_api.config import app, db
from kpo_dist_api.models import Concert, concert_schema

SEED_DATA = [
    {
        "season": "Spring 2023",
        "title": "Ticket to Ride",
    },
    {
        "season": "Fall 2023",
        "title": "Liberty Belles",
    },
    {
        "season": "Christmas 2023",
        "title": "Christmas at the Movies",
    },
    {
        "season": "March 2024",
        "title": "Tribute to John Williams",
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in SEED_DATA:
        new_concert = Concert(season=data.get("season"), title=data.get("title"))
        db.session.add(new_concert)
    db.session.commit()
    concert = Concert.query[0]
    print(concert_schema.dump(concert))
