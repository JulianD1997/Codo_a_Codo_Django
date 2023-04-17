from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password


class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    user = models.CharField(max_length=50, null=False,
                            unique=True, blank=False)
    email = models.EmailField(
        max_length=70, null=False, unique=True, blank=False, validators=[validate_email])
    password = models.CharField(max_length=128, null=False, blank=False)

    class Meta:
        db_table = 'user'
        ordering = ['last_name', 'name']

    def __str__(self):
        return f"{self.name} {self.last_name} ({self.user})"

    def get_full_name(self):
        return f"{self.name} {self.last_name}"
    
    @property
    def is_authenticated(self):
        return True
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.last_name = self.last_name.capitalize()
        super().save(*args, **kwargs)