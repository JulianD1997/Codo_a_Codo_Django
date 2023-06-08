from django.urls import path

from .views import get_genres, get_list_movie

urlpatterns = [
    path("movie/genres", get_genres, name="movies_genres"),
    path('page/<slug:action>', get_list_movie, name="list_movies")    
]
