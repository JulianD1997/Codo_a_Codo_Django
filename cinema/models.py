from django.db import models
from users.models import User

# Create your models here.


class Films(models.Model):
    id_films = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gender(models.Model):
    id_gender = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.gender


class Likes(models.Model):
    id_likes = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    films = models.ForeignKey(Films, on_delete=models.CASCADE)

    def __str__(self):
        return self.films
