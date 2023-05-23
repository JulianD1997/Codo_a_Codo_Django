from django.shortcuts import render
from API_TMDB.views import tmdb_api
from django.http import HttpResponse
# Create your views here.
def get_genres(request):
    _request = tmdb_api('genre/movie','list')
    context = {'genres' : _request.json()['genres']}

    return render(request,'movies/search_movie.html',context=context)