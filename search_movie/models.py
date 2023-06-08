from django.db import models
from users.models import User
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film_id = models.CharField(max_length=10)
# Create your models here.
