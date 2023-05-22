from django.db import models
from users.models import User
from django.core.validators import validate_email


# Create your models here.

class Classification(models.Model):
    atp=models.CharField(max_length=50)
    pm_13=models.CharField(max_length=50)
    pm_16=models.CharField(max_length=50)
    pm_18=models.CharField(max_length=50)


class Films(models.Model):
    id_films=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    director=models.CharField(max_length=50)
    gender=models.CharField(max_length=30)
    classification=models.OneToOneField(Classification, on_delete=models.CASCADE )#Establecemos una relacion de 1 a1 con Classificatin
    
    def __str__(self):
        return self.name
    
    
class Suscriber(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    user = models.CharField(max_length=50, null=False, unique=True, blank=False)
    email = models.EmailField(max_length=70, null=False, unique=True, blank=False, validators=[validate_email])
    password = models.CharField(max_length=128, null=False, blank=False)
    film=models.ForeignKey(Films, on_delete=models.CASCADE ) # Establecemos la relacion de 1 a muchos

    def __str__(self):
        return self.name
    
    
class Gender(models.Model):
    id_gender=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    gender=models.CharField(max_length=30) 
    
    def __str__(self):
        return self.name
    
class Likes(models.Model):
    id_likes=models.AutoField(primary_key=True)
    suscriber=models.ForeignKey(Suscriber,on_delete=models.CASCADE)#Establecemos la relacion de 1 a muchos
    film=models.ManyToManyField(Films)#Establecemos la relacion de MUchos a Muchos

    def __str__(self):
        return f'{self.user.name}likes{self.film.name}'









       

