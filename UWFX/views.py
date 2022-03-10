from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from UWFX.forms import addFilmForm, addShowingForm
from UWFX.forms import deleteFilmForm
from UWFX.forms import addScreenForm
from UWFX.models import Film
from UWFX.models import Showing

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