from operator import add
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from UWFX.forms import  *
from UWFX.forms import deleteFilmForm
from UWFX.forms import addScreenForm
from UWFX.models import Film
from UWFX.models import Showing
from datetime import date

def home(request):
    return render(request, "UWFX/home.html")

def addFilm(request):
    context = {}
    form = addFilmForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Film details successfully added.")
            return redirect('/addFilm')

    context['form'] = form
    return render(request, "UWFX/addFilm.html", context)

def deleteFilm(request):
    context = {}
    form = deleteFilmForm(request.GET or None)
    Showing.objects.filter(date__lt = date.today()).delete()

    if request.method == "GET":
        if form.is_valid():
            if Showing.objects.filter(film_id = request.GET['delete_film']):
                messages.warning(request, "Cannot delete as showing exists for selected film.")
            else:
                Film.objects.filter(id=request.GET['delete_film']).delete()
                messages.success(request, "Film details successfully deleted.")

    context['form'] = form
    return render(request, "UWFX/deleteFilm.html", context)

def addScreen(request):
    context = {}
    form = addScreenForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Screen successfully added.")
            return redirect('/addScreen')

    context['form'] = form
    return render(request, "UWFX/addScreen.html", context)

def addShowing(request):
    context = {}
    form = addShowingForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Showing successfully added.")
            return redirect('/addShowing')

    context['form'] = form
    return render(request, "UWFX/addShowing.html", context)


def addClubDetails(request):
    context = {}
    clubForm = addClubForm(request.POST or None)
    repForm = addRepForm(request.POST or None)
    if request.method == "POST":
        if clubForm.is_valid() and repForm.is_valid():
            rep = repForm.save()
            
            club = clubForm.save(commit=False)
            club.rep = rep
            club.save()
            messages.success(request, "Club Registered Successfully.")
            return redirect('/addClubDetails')

    context = {
        'clubForm': clubForm,
        'repForm': repForm,
    }
    return render(request, "UWFX/addClub.html", context)


def deleteClub(request):
    context = {}
    form = deleteClubForm(request.GET or None)

    if request.method == "GET":
        if form.is_valid():
            Club.objects.filter(id=request.GET['delete_club']).delete()
            messages.success(request, "Club details successfully deleted.")

    context['form'] = form
    return render(request, "UWFX/deleteClub.html", context)
