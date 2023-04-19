from django.db import models
    
class File(models.Model):
    """One page of a Part"""
    url = models.FilePathField() #TODO: How to define FilePathField

    # TODO: Can we get the number of pages in a PDF programmatically?
    page_num = models.IntegerField("Page Number")
    created_dt = models.DateTimeField("Created Date", auto_now_add=True)
    modified_dt = models.DateTimeField("Last Modified", auto_now=True)

    def __str___(self):
        return self.url


class Part(models.Model):
    """Instrument part for a Song"""
    name = models.CharField(max_length=20)
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str___(self):
        return self.name


class Song(models.Model):
    """Single song in a Concert"""
    title = models.CharField(max_length=200)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)

    def __str___(self):
        return self.title


class Concert(models.Model):
    """Set of Performaces for a certain set of Songs"""

    class Season(models.IntegerChoices):
        """Choices for Concert.season"""
        FALL = 1
        CHRISTMAS = 2
        FEBRUARY = 3
        SPRING = 4

    title = models.CharField(max_length=200)
    season = models.IntegerField(choices=Season.choices) # Not confused with "Concert Season" like 2022-2023
    song = models.ManyToManyField(Song, related_name="concerts")

    def __str___(self):
        return self.title


class Performance(models.Model):
    """Performance date for a concert"""

    performance_date = models.DateTimeField("Performance Date")
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)

    def __str__(self):
        return self.performance_date