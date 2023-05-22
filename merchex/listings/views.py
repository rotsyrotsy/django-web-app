from django.shortcuts import render
from django.http import HttpResponse
from listings.models import *

def songs(request):
    songs = Song.objects.all()
    return render(request,
                  "listings/songs.html",
                  {"songs":songs})

def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  "listings/band_list.html",
                  {"bands":bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  "listings/band_detail.html",
                  {'band':band})

def about(request):
    return HttpResponse("<h1>A propos</h1><p>Nous adorons merch!</p>")

def contact(request):
    return HttpResponse("<h1>Contactez-nous</h1><p>Contact au 034 55 000 00.</p>")