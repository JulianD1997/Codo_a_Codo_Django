from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Crea y guarda un usuario con el correo electrónico y la contraseña proporcionados.
        """
        if not email:
            raise ValueError('Debe ingresar un correo electrónico válido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crea y guarda un superusuario con el correo electrónico y la contraseña proporcionados.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    user = models.CharField(max_length=50, null=False,
                            unique=True, blank=False)
    email = models.EmailField(
        max_length=70, null=False, unique=True, blank=False, validators=[validate_email])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'user']
    
    objects = UserManager()

    class Meta:
        db_table = 'user'
        ordering = ['last_name', 'name']
# 
    def __str__(self):
        return f"{self.name} {self.last_name} ({self.user})"

    def get_full_name(self):
        return f"{self.name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.last_name = self.last_name.capitalize()
        super().save(*args, **kwargs)