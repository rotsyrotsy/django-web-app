from django.shortcuts import render,redirect  
from django.http import HttpResponse
from listings.models import *
from listings.forms import *
from django.core.mail import send_mail

def song_list(request):
    songs = Song.objects.all()
    return render(request,
                  "listings/song_list.html",
                  {"songs":songs})

def song_detail(request, id):
    song = Song.objects.get(id=id)
    return render(request,
                  "listings/song_detail.html",
                  {'song':song})

def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('song-detail',song.id)
    else:
        form = SongForm
    return render(request,
                  "listings/song_create.html",
                  {'form':form})

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

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail',band.id)
    else:
        form = BandForm
    return render(request,
                  "listings/band_create.html",
                  {'form':form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail',band.id)
    else:
        form=BandForm(instance=band)
    return render(request,"listings/band_update.html",
                  {'form':form})

def band_delete(request,id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    
    return render(request,"listings/band_delete.html",
                  {'band':band})

def about(request):
    return HttpResponse("<h1>A propos</h1><p>Nous adorons merch!</p>")

def contact(request):
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        return redirect('contact')
    else:
        form = ContactUsForm()
    return render(request,"listings/contact.html",
                  {'form':form})