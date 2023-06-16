from django.urls import path

from .views import movie, popular, search, indexc, now

urlpatterns = [
    path('movie.html', movie, name="movie"),
    path('popular.html', popular, name="popular"),
    path('search.html', search, name="search"),
    path('indexc.html', indexc, name="indexc"),
    path('now-playing.html', now, name="now"),
    
]


