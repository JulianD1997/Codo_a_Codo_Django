from django.urls import path

from .views import get_video, movies_json

urlpatterns = [
    path("movie/", movies_json, name="movies_json"),
    path("movie/<int:id>/", get_video, name="get_video"),
]
