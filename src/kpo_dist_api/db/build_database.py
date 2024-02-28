from kpo_dist_api.config import app, db
from kpo_dist_api.models import Concert, Song, concert_schema, song_schema

from icecream import ic

SEED_DATA = [
    {
        "season": "Spring 2023",
        "title": "Ticket to Ride",
        "songs": [
            {"title": "Music from Up"},
            {"title": "Top Gun"},
        ]
    },
    {
        "season": "Fall 2023",
        "title": "Liberty Belles",
        "songs": [
            {"title": "Washington Post"},
            {"title": "Armed Forces Medley"},
            {"title": "The Cowboys"}
        ]
    },
    {
        "season": "Christmas 2023",
        "title": "Christmas at the Movies",
        "songs": [
            {"title": "The Holiday"},
            {"title": "Cool Yule"},
        ]
    },
    {
        "season": "March 2024",
        "title": "Tribute to John Williams",
        "songs": [
            {"title": "Far and Away"},
            {"title": "Adventures on Earth"},
            {"title": "The Cowboys"},
        ]
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    add_concerts_list = []
    add_songs_list = []
    for data in SEED_DATA:
        ic(data)
        new_concert = Concert(season=data.get("season"), title=data.get("title"))
        songs_list = data.get("songs")
        for song in songs_list:
            ic(song)
            add_song = next((repeated_song for repeated_song in add_songs_list if repeated_song.title == song["title"]), None)
            ic(type(add_song), add_song)
            if not add_song:
                add_song = Song(title=song.get("title"))
                add_songs_list.append(add_song)
            new_concert.songs.append(add_song)
        add_concerts_list.append(new_concert)
    ic(add_songs_list, add_concerts_list)
    db.session.add_all(add_songs_list)
    db.session.add_all(add_concerts_list)
    db.session.commit()
    concert = Concert.query[0]
    print(concert_schema.dump(concert))
