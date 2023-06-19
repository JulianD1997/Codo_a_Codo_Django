from django.urls import path

from .views import get_genres, get_list_movie,like_movie

urlpatterns = [
    path("movie/genres", get_genres, name="movies_genres"),
    path('page/', get_list_movie, name="page"),
    path('page/<str:genre>/', get_list_movie, name="page_genre"),
    path('like/',like_movie, name='like_movie')
]