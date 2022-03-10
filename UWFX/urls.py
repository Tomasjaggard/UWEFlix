from django.urls import path
from UWFX import views

urlpatterns = [
    path("", views.home, name="home"),
    path("addFilm/", views.addFilm, name="addFilm"),
    path("deleteFilm/", views.deleteFilm, name="deleteFilm"),
]