from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    MovieID = models.AutoField(primary_key=True)
    MovieTitle = models.CharField("Movie Title",max_length=200)
    Actor1Name = models.CharField("Lead Actor",max_length=100)
    Actor2Name = models.CharField("Supporting Actor",max_length=100, blank=True, null=True)
    DirectorName = models.CharField("Director",max_length=100)
    MovieGenre = models.CharField("Genre",max_length=50)
    ReleaseYear = models.PositiveIntegerField("Release Year")

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"