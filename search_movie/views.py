import json
from django.shortcuts import render
from API_TMDB.views import movies_json, tmdb_api

# Create your views here.
def get_genres():
    _request = tmdb_api('genre/movie','list')

    return _request.json()['genres']

def get_list_movie(request):
    genres = get_genres()
    movies = movies_json(request).content.decode("utf-8")
    context = {"movies": json.loads(movies),
               'genres' : genres}

    return render(request,'movies/search_movie.html',context=context)
