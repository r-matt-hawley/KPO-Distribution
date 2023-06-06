import csv
from django.core.files import File as NewFile
from music.models import Concert, Performance, Song, Part, File
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
SCRIPT_DIR = Path(__file__).resolve().parent

def run():
    with open(SCRIPT_DIR / 'setup_db_data/data.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Concert.objects.all().delete()
        Song.objects.all().delete()
        Part.objects.all().delete()
        File.objects.all().delete()

        for row in reader:
            print(row)

            concert, _ = Concert.objects.get_or_create(title=row[0])
            song, _ = concert.songs.get_or_create(title=row[1])
            part, _ = song.parts.get_or_create(name = row[2])

            file_name = row[3].split("/")[-1]
            file = File(part=part, song=song, file_name=file_name)
            with open(SCRIPT_DIR / row[3], 'rb') as pdf_file:
                file.pdf.save(file_name, NewFile(pdf_file), save=True)
            
            concert.save()
            song.save()
            part.save()
            file.save()
