import requests
from django.http.response import JsonResponse
from django.shortcuts import  render, redirect
from django.http import HttpResponse


import json
from API_TMDB.views import movies_json



def movie(request  ):

    return render(request, 'cinema/movie.html')

def popular(request):
    return render(request, 'cinema/popular.html')

def search(request):
    return render(request, 'cinema/search.html')

def indexc(request):
   return render(request, 'cinema/indexc.html')

def now(request):
    return render(request, 'cinema/now-playing.html')





   
   
   
   
   

 
 
 

 
 
 
 
 

 
 





















