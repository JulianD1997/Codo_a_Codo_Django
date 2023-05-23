from django.urls import path
from . import views

urlpatterns = [
        path('administration/', views.create_films, name="create_films"),
]