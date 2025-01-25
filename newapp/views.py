from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.

def movie_list(request):
   movie_objects = Movies.objects.all()
   paginator = Paginator(movie_objects,4)
   page = request.GET.get('page') 
   movie_objects = paginator.get_page(page)
   return render(request,'newapp/movies_list.html',{'movies_objects':movie_objects})
   # return HttpResponse("hello")