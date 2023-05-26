from django.db import models


class Concert(models.Model):
    """Set of Performaces for a certain set of Songs"""

    class Season(models.IntegerChoices):
        """Choices for Concert.season"""
        FALL = 1
        CHRISTMAS = 2
        FEBRUARY = 3
        SPRING = 4

    title = models.CharField("Concert Title", max_length=200)
    season = models.IntegerField(choices=Season.choices, default=Season.FALL) # Not confused with "Concert Season" like 2022-2023

    def __str__(self):
        return f"{self.title}"   


class Song(models.Model):
    """Single song in a Concert"""
    title = models.CharField("Song Title", max_length=200)
    concert = models.ManyToManyField(Concert, blank=True, related_name="songs")

    def __str__(self):
        return f"{self.title}"


class Part(models.Model):
    """Instrument part for a Song"""
    name = models.CharField("Part Name", max_length=20)

    # We need to know what songs each part has, and
    # we need to know what parts each song has.
    songs = models.ManyToManyField(Song, blank=True, related_name="parts")


    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class File(models.Model):
    """One page of a Part"""

    # We need to know what song and part this file is associated with
    part = models.ForeignKey(Part, blank=True, null=True, on_delete=models.SET_NULL)
    song = models.ForeignKey(Song, blank=True, null=True, on_delete=models.CASCADE)

    # TODO: Complete tutorial on uploading pdf files
    # https://www.askpython.com/django/upload-files-to-django
    file_name = models.CharField(max_length = 100)
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True) 

    # TODO: Can we get the number of pages in a PDF programmatically?
    # page_num = models.IntegerField("Page Number", default=1)
    created_dt = models.DateTimeField("Created Date", auto_now_add=True)
    modified_dt = models.DateTimeField("Last Modified", auto_now=True)

    def __str__(self):
        return f"{self.file_name}"


class Performance(models.Model):
    """Performance date for a concert"""

    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    performance_date = models.DateTimeField("Performance Date")

    def __str__(self):
        return f"{self.performance_date}"