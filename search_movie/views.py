import json
from django.shortcuts import render
from API_TMDB.models.movies import Movie
from API_TMDB.views import movies_json, tmdb_api

global page
page = 1
# Create your views here.
def get_genres():
    _request = tmdb_api('genre/movie','list')

    return _request.json()['genres']

def get_list_movie(request,pagination= '', genre = ''):
    global page
    params = {}
    if len(genre)> 1:
        page = 1
        params["with_genres"] = genre
        
    if pagination == 'next':
        page += 1
    
    if pagination == 'prev' and page > 1:
        page -= 1
    params["sort_by"] = "popularity.desc"
    params["page"] = page
    
    genres = get_genres()
    print(params)
    movies_request = tmdb_api(
                params=params
            )
    movies = [
                Movie(movie).to_dict() for movie in movies_request.json()['results']
            ]
    context = {"movies": movies,
               'genres' : genres}

    return render(request,'movies/search_movie.html',context=context)
