from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birth = models.DateField()

    class Meta:
        db_table = "actor"

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    run_time = models.IntegerField()
    actor = models.ManyToManyField('Actor')

    class Meta:
        db_table = "movie"

