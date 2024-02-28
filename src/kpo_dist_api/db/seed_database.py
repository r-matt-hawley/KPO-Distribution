from kpo_dist_api.config import app, db
from kpo_dist_api.models import Concert, Song

from icecream import ic

concert1 = Concert(season="Spring 2023", title="Ticket to Ride")
concert2 = Concert(season="Fall 2023", title="Victory Bells")
concert3 = Concert(season="Christmas 2023", title="Christmas at the Movies")
concert4 = Concert(season="March 2024", title="Tribute to John Williams")

song1 = Song(title='Music from up')
song2 = Song(title='Top Gun')
song3 = Song(title='Washington Post')
song4 = Song(title='Armed Forces Medley')
song5 = Song(title='The Cowboys')
song6 = Song(title='The Holiday')
song7 = Song(title='Cool Yule')
song8 = Song(title='Far and Away')
song9 = Song(title='Adventures on Earth')

concert1.songs.append(song1)
concert1.songs.append(song2)
concert2.songs.append(song3)
concert2.songs.append(song4)
concert2.songs.append(song5)
concert3.songs.append(song6)
concert3.songs.append(song7)
concert4.songs.append(song8)
concert4.songs.append(song9)
concert4.songs.append(song5)

with app.app_context():    
    db.drop_all()
    db.create_all()

    db.session.add_all([concert1, concert2, concert3, concert4])
    db.session.add_all([song1, song2, song3, song4, song5, song6, song7, song8, song9])

    db.session.commit()