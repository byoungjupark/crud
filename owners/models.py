from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=2000)
    age = models.IntegerField()

    class Meta:
        db_table = 'owner'

class Dog(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    age = models.IntegerField()

    class Meta:
        db_table = 'dog'
