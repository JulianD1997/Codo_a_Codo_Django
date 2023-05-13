from django.forms import ModelForm, NumberInput, Select, Textarea, TextInput, EmailInput, PasswordInput
from django.utils.translation import gettext_lazy as _

from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','last_name','user','email','password']
        
        labels = {
            'name':_('Nombre'),
            'last_name':_('Apellido'),
            'user':_('Usuario'),
            'email':_('Email'),
            'password':_('Contraseña'),
        }
        widgets = {
            'name' : TextInput(attrs={'class':'form__input'}),
            'last_name' : TextInput(attrs={'class':'form__input'}),
            'user' : TextInput(attrs={'class':'form__input'}),
            'email' : EmailInput(attrs={'class':'form__input'}),
            'password': PasswordInput(attrs={'class':'form__input'})
        }
        error_messages = {
            'user': {
                'unique': 'Este nombre de usuario ya existe. Por favor, elige otro.',
            },
            'email': {
                'unique': 'Este correo ya está registrado en nuestro sistema. Por favor, utiliza otro correo.',
            },
        }