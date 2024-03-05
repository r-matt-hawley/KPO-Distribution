from kpo_dist_api.config import app, db
from kpo_dist_api.models import Concert, Song, Part, concert_schema, song_schema, parts_schema

from icecream import ic

SEED_DATA = [
    {
        "season": "Spring 2023",
        "title": "Ticket to Ride",
        "songs": [
            {
                "title": "Music from Up",
                "parts": [
                    {"name": "Flute"},
                    {"name": "Trumpet"},
                ]
            },
            {
                "title": "Top Gun",
                "parts": [
                    {"name": "Flute"},
                    {"name": "Trumpet"},
                ]
            },
        ]
    },
    {
        "season": "Fall 2023",
        "title": "Liberty Belles",
        "songs": [
            {
                "title": "Washington Post",
                "parts": [
                    {"name": "Flute"},
                    {"name": "Trumpet"},
                ]
            },
            {
                "title": "Armed Forces Medley",
                "parts": [
                    {"name": "Flute"},
                    {"name": "Trumpet"},
                ]
            },
            {"title": "The Cowboys",
                "parts": [
                    {"name": "Flute"},
                    {"name": "Trumpet"},
                ]
            }
        ]
    },
    {
        "season": "Christmas 2023",
        "title": "Christmas at the Movies",
        "songs": [
            {
                "title": "The Holiday",
                "parts": [
                    {"name": "Flute"},
                    {"name": "Trumpet"},
                ]
            },
            {
                "title": "Cool Yule",
                "parts": [
                    {"name": "Flute"},
                    {"name": "Trumpet"},
                ]
            },
        ]
    },
    {
        "season": "March 2024",
        "title": "Tribute to John Williams",
        "songs": [
            {
                "title": "Far and Away",
                "parts": [
                    {"name": "Flute"},
                    {"name": "Trumpet"},
                ]
            },
            {
                "title": "Adventures on Earth",
                "parts": [
                    {"name": "Flute"},
                    {"name": "Trumpet"},
                ]
            },
            {
                "title": "The Cowboys",
                "parts": [
                    {"name": "Flute"},
                    {"name": "Trumpet"},
                ]
            },
        ]
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    add_concerts_list = []
    add_songs_list = []
    add_parts_list = []
    for data in SEED_DATA:
        ic(data)
        new_concert = Concert(season=data.get("season"), title=data.get("title"))
        songs_list = data.get("songs")
        for song in songs_list:
            ic(song)
            # Check if the current song has already been added to the database
            add_song = next((repeated_song for repeated_song in add_songs_list if repeated_song.title == song["title"]), None)
            ic(type(add_song), add_song)
            if not add_song:
                # The first occurance of this song
                add_song = Song(title=song.get("title"))
                add_songs_list.append(add_song)
            parts_list = song.get("parts")
            for part in parts_list:
                ic(part)
                # Check if the current part has already been added to the database
                add_part = next((repeated_part for repeated_part in add_parts_list if repeated_part.name == part["name"]), None)
                if not add_part:
                    # The first occurance of this part
                    add_part = Part(name=part.get("name"))
                    add_parts_list.append(add_part)
                ic(type(add_part), add_part)
                add_song.parts.append(add_part)
            new_concert.songs.append(add_song)
        add_concerts_list.append(new_concert)
    ic(add_parts_list, add_songs_list, add_concerts_list)
    db.session.add_all(add_parts_list)
    db.session.add_all(add_songs_list)
    db.session.add_all(add_concerts_list)
    db.session.commit()
    concert = Concert.query[0]
    print(concert_schema.dump(concert))
    song = Song.query[0]
    print(song_schema.dump(song))
    parts = Part.query.all()
    print(parts_schema.dump(parts))
