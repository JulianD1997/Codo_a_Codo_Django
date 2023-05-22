from django.urls import path
from . import views

urlpatterns = [
        path('administration/', views.film_admin, name="film_admin"),
]