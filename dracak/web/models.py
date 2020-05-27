from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=256)
    place = models.CharField(max_length=128, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="characters")


class Place(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    text = models.TextField()
    options = models.ManyToManyField("Option")

    def __str__(self):
        return self.name


class Option(models.Model):
    text = models.TextField()
    next_place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text
