from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse

# Create your views here.

def movie_list(request):
   movie_objects = Movies.objects.all()
   # return render(request,'newapp/movies_list.html',{'movies_objects':movie_objects})
   return HttpResponse("hello")