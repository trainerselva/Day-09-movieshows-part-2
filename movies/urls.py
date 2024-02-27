from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    # path("<int:id>", views.movie_detail, name="movie-detail"),
    path("<slug:slug>", views.movie_detail, name="movie-detail"),
]