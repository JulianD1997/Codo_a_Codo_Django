from django.urls import path

from .views import get_genres, get_list_movie

urlpatterns = [
    path("movie/genres", get_genres, name="movies_genres"),
    path('page/', get_list_movie, name="list_movies"),  
    path('page/<slug:pagination>/<slug:genre>/', get_list_movie, name="list_movies"),
    path('page/<slug:genre>/', get_list_movie, name="list_movies")   
]

