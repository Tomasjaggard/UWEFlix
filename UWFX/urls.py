from django.urls import path
from UWFX import views

urlpatterns = [
    path("", views.home, name="home"),
    path("addFilm/", views.addFilm, name="addFilm"),
    path("deleteFilm/", views.deleteFilm, name="deleteFilm"),
    path("addScreen/", views.addScreen, name="addScreen"),
    path("addShowing/", views.addShowing, name="addShowing"),
    path("addClubDetails/", views.addClubDetails, name="addClubDetails"),
    path("deleteClub/", views.deleteClub, name="deleteClub"),
]