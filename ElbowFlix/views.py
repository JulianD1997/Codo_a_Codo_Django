import json

from django.shortcuts import redirect, render
from API_TMDB.views import movies_json
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    Renderiza la página principal con una lista de películas.
    """
    movies = movies_json(request).content.decode("utf-8")
    context = {"movies": json.loads(movies)[:10]}

    return render(request, "index.html", context)
