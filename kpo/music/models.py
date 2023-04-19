from django.db import models

class Concert(models.Model):

    class Season(models.IntegerChoices):
        FALL = 1
        CHRISTMAS = 2
        FEBRUARY = 3
        SPRING = 4

    title = models.CharField(max_length=200)
    season = models.IntegerField(choices=Season.choices, )
    performance_date = models.DateTimeField("Performance Date")

    def __str___(self):
        return f"{self.season} {self.performance_date.year}, {self.title}"


class Song(models.Model):
    title = models.CharField(max_length=200)
    concert = models.ManyToManyField(Concert, related_name="songs")

    def __str___(self):
        return self.title


class Part(models.Model):
    name = models.CharField(max_length=20)

    def __str___(self):
        return self.name


class File(models.Model):
    title = models.CharField(max_length=200) # TODO: Is this needed?
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    created_dt = models.DateTimeField("Created Date")
    modified_dt = models.DateTimeField("Last Modified", auto_now=True)

    def __str___(self):
        return f"{self.song}/{self.part}"

