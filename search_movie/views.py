from django.shortcuts import render
from API_TMDB.views import tmdb_api

# Create your views here.
def get_genres(request):
    _request = tmdb_api('genre/movie','list')
    context = {'genres' : _request.json()['genres']}

    return render(request,'movies/search_movie.html',context=context)

def get_movies(request):
    """
    Renderiza la página principal con una lista de películas.
    """
    movies = movies_json(request).content.decode("utf-8")
    context = {"movies": json.loads(movies)}

    return render(request, "index.html", context)