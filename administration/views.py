from django.shortcuts import render, redirect
from administration.forms import ClassificationForm, FilmsForm, SuscriberForm, LikesForm
from administration.models import  Films, Suscriber, Gender, Likes, Classification
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.

def create_films(request):
    form = FilmsForm()  # Crea una instancia del formulario FilmsForm

    context = {
        'form': form,  # Agrega el formulario al contexto
    }

    return render(request, 'administration/index_admin.html', context)



























