from django.shortcuts import render
from .models import Movies

# Create your views here.

def movie_list(request):
   movie_objects = Movies.object.all()
   return render(request,'newapp/movies_list.html',{'movies_objects':movie_objects})