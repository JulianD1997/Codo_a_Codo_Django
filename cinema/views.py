import requests
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
import json

def movie(request):
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=es-MX&page=1&sort_by=popularity.desc"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMTAwMDk1YTlmOTZkMjVkMmYzYTJmNjljYTg0OGU1YiIsInN1YiI6IjY0NDQ3Yjc3MDU4MjI0MDUzZDMyZWE3YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dZ2DSVFZwUWXoaoib-DMm0HMXti8GuF-18rn4IBbohM"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
     # Aquí puedes procesar los datos recibidos y renderizar la plantilla
    return render(request,'cinema/movies.html',{'data':data})

 
 
 

 
 
 
 
 

 
 




















