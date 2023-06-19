import json
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from API_TMDB.models.movies import Movie
from API_TMDB.views import movies_json, tmdb_api
from users.models import User
from .models import Like

gen = ''
page = 1

def get_genres():
    _request = tmdb_api('genre/movie', 'list')
    return _request.json()['genres']

def get_list_movie(request, genre='', pag=''):
    global gen
    global page
    params = {}
    if 'pag' in request.GET:
        pag = request.GET['pag']
        genre = request.GET['genre']

    if genre != '':
        if genre == gen:
            params["with_genres"] = genre
        else:
            params["with_genres"] = genre
            gen = genre
            page = 1
    elif genre == '' and pag == '':
        page = 1
    
    if pag == 'next':
        page += 1
    elif pag == 'prev' and page > 1:
        page -= 1

    params["sort_by"] = "popularity.desc"
    params["page"] = page

    genres = get_genres()
    movies_request = tmdb_api(params=params)
    movies = [Movie(movie).to_dict() for movie in movies_request.json()['results']]

    context = {
        "movies": movies,
        'genres': genres,
        'gen': genre
    }

    return render(request, 'movies/search_movie.html', context=context)

@login_required
def like_movie(request):
    if request.method == 'GET':
        movie_id = request.GET.get('movie_id')
        user = request.user

        # Guardar la película como favorita o gusto del usuario
        Like.objects.create(user=user, film_id=movie_id)

    return redirect('page')