from django import forms
from .models import Films, Suscriber, Gender, Likes, Classification


# Asociamos el modelo con el formulario

class FilmsForm(forms.ModelForm):
    class Meta:
        model= Classification
        fields='__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form__input'}),
            'director' : forms.TextInput(attrs={'class':'form__input'}),
            'gender' : forms.TextInput(attrs={'class':'form__input'}),
            'classification' : forms.TextInput(attrs={'class':'form__input'}),
}

class ClassificationForm(forms.ModelForm):
    
    class Meta:
        model=Films
        fields= '__all__'
        widgets = {
             'atp' : forms.TextInput(attrs={'class':'form__input'}),
             'pm_13' : forms.TextInput(attrs={'class':'form__input'}),
             'pm_16' : forms.TextInput(attrs={'class':'form__input'}),
             'pm_18' : forms.TextInput(attrs={'class':'form__input'}),
        }
        
class SuscriberForm(forms.ModelForm):
    
    class Meta:
        model=Suscriber
        fields= '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form__input'}),
            'last_name' : forms.TextInput(attrs={'class':'form__input'}),
            'user' : forms.TextInput(attrs={'class':'form__input'}),
            'email' : forms.TextInput(attrs={'class':'form__input'}),
        }
        
class LikesForm(forms.ModelForm):
    
    class Meta:
        model = Likes
        fields = "__all__"
        widgets = {
    'suscriber' : forms.TextInput(attrs={'class':'form__input'}),
    'film' : forms.TextInput(attrs={'class':'form__input'}),
    }
        

           
        
           
   
   
   
   
   
   

   









        
    
        
        
    
        
        
    
        
    