from django.test import TestCase
from music.models import Concert, Song, Part


class ConcertModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create table data which will be created before any tests are run"""
        Concert.objects.create(title="Ticket to Ride", season=Concert.Season.SPRING)

    def setUp(self):
        """Create table data which will refresh before each test"""
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_concert_title(self):
        concert = Concert.objects.get(id=1)
        field_label = concert._meta.get_field('title').verbose_name
        self.assertEqual(field_label, "Concert Title")

    def test_object_name_is_concert_title(self):
        concert = Concert.objects.get(id=1)
        expected_object_name = "Ticket to Ride"
        self.assertEqual(str(concert), expected_object_name)


class SongModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create table data which will be created before any tests are run"""
        Song.objects.create(title="Music from Up")

    def test_object_name_is_song_title(self):
        song = Song.objects.get(id=1)
        expected_object_name = "Music from Up"
        self.assertEqual(str(song), expected_object_name)


class PartModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create table data which will be created before any tests are run"""
        Part.objects.create(name="Flute 1")

    def test_object_name_is_song_title(self):
        part = Part.objects.get(id=1)
        expected_object_name = "Flute 1"
        self.assertEqual(str(part), expected_object_name)


class ModelRelationshipsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create table data which will be created before any tests are run"""
        concert_fall = Concert.objects.create(title="Fall Test")
        song_top_gun = Song.objects.create(title="Top Gun")
        part_fl_1 = Part.objects.create(name="Flute 1", song=song_top_gun)

        concert_ttr = Concert.objects.create(title="Ticket to Ride", season=Concert.Season.SPRING)
        song_up = Song.objects.create(title="Music from Up")
        part_fl_2 = Part.objects.create(name="Flute 2")

    def test_add_song_to_concert(self):
        concert_fall = Concert.objects.get(title="Fall Test")
        song_tg = Song.objects.get(title="Top Gun")
        song_tg.concert.add(concert_fall)
        self.assertEqual(song_tg.concert.get(), concert_fall)
        self.assertEqual(concert_fall.songs.get(), song_tg) # type: ignore

    def test_song_has_one_part(self):
        song = Song.objects.get(title="Top Gun")
        part = Part.objects.get(name="Flute 1")
        self.assertEqual(song, part.song)

    def test_num_parts_is_2(self):
        num_parts = Part.objects.all().count()
        self.assertEqual(num_parts, 2)

    def test_add_part_to_song(self):
        song = Song.objects.get(title="Top Gun")
        part = Part.objects.get(name="Flute 2")
        part.song=song
        part.save()
        self.assertQuerysetEqual(song.part_set.all(), Part.objects.all(), ordered=False) # type: ignore

    def test_query_concert_song_part(self):
        concert = Concert.objects.get(title="Ticket to Ride")
        song = Song.objects.get(title="Music from Up")
        part = Part.objects.get(name="Flute 1")

        # Implement relationships
        song.concert.add(concert)
        part.song=song

        # query concert from part
        # self.assertEqual(concert.song_set.filter(part__name__contains("Flute")), part.name)
