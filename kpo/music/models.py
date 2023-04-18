from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Season(models.Model):
    name = models.CharField(max_length=10)

    def __str___(self):
        return self.name


class Concert(models.Model):
    title = models.CharField(max_length=200)
    season = models.ForeignKey(Season)
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

