from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.

def movie_list(request):
   movie_objects = Movies.objects.all()

   # search and filtering part
   movie_name = request.GET.get('movie_name')  # get the movie name from the search bar

   if movie_name !='' and movie_name is not None:
      movie_objects = movie_objects.filter(name__icontains=movie_name)    # icontains gives the movie also by typing only one word of movie 



   # pagination part
   paginator = Paginator(movie_objects,4)     # It divide the movie in 4 groups
   page = request.GET.get('page') 
   movie_objects = paginator.get_page(page)
   return render(request,'newapp/movies_list.html',{'movies_objects':movie_objects})
   # return HttpResponse("hello")