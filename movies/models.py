from django.db import models
from users.models import User
# Create your models here.
class Film(models.Model):
    id_film = models.IntegerField(blank=False,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)