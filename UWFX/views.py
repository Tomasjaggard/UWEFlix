from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from UWFX.forms import addFilmForm
from UWFX.forms import deleteFilmForm
from UWFX.models import Film

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "UWFX/home.html")

def addFilm(request):
    context = {}
    form = addFilmForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Film details successfully added.")

    context['form'] = form
    return render(request, "UWFX/addFilm.html", context)

def deleteFilm(request):
    context = {}
    form = deleteFilmForm(request.GET or None)

    if request.method == "GET":
        if form.is_valid():
            Film.objects.filter(id=request.GET['delete_film']).delete()
            messages.success(request, "Film details successfully deleted.")

    context['form'] = form
    return render(request, "UWFX/deleteFilm.html", context)
