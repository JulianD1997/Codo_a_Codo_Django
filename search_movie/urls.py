from django.urls import path

from .views import get_genres

urlpatterns = [
    path("movie/genres", get_genres, name="movies_genres"),
    
]
