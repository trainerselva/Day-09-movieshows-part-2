from django.shortcuts import render
from django.http import Http404

from django.shortcuts import get_object_or_404

# Create your views here.

# Get all the models to use
from .models import Movie

def index(request):
    all_movies = Movie.objects.all()
    return render(request, "movies/index.html", {
        "all_movies": all_movies
    })


# def movie_detail(request, id):
#     # try:
#     #     # movie = Movie.objects.get(id=id)

#     #     # Alternate method of getting the required object
#     #     # Here pk indicates primary key

#     #     movie = Movie.objects.get(pk=id)
#     # except:
#     #     raise Http404
    
#     movie = get_object_or_404(Movie, pk=id)

#     return render(request, "movies/movie_detail.html", {
#         "title": movie.title,
#         "mainactor": movie.mainactor,
#         "rating": movie.rating,
#         "is_boxofficehit": movie.is_boxofficehit
#     })

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    return render(request, "movies/movie_detail.html", {
        "title": movie.title,
        "mainactor": movie.mainactor,
        "rating": movie.rating,
        "is_boxofficehit": movie.is_boxofficehit
    })