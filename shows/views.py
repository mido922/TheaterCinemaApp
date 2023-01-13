from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import newShow
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import get_object_or_404
import re


# Create your views here.

def show_list(request):
  shows = newShow.objects.all().order_by('date',)
  return render(request, 'availableShows.html', {'shows':shows})



def addNewMovie(request):
  print(request)
  if request.method == 'POST':
    form = forms.addNewShow(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.slug = instance.title.lower().replace(" ", "-")
      
      instance.save()
      return redirect('shows:list')
    else:
      return render(request, 'addNewMovie.html')

  else:
    form = forms.addNewShow()
    # field = form.fields['slug']
    # field.widget = field.hidden_widget()
  return render(request, 'addNewMovie.html', {'form':form})

def editMovieList(request):
  shows = newShow.objects.all().order_by('date',)
  return render(request, 'editMovieList.html', {'shows':shows})

def editMovieDetails(request,slug):
  if request.method == 'POST':
    form = forms.addNewShow(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('shows:list')
  else:
    movie = newShow.objects.get(slug=slug)
    form = forms.addNewShow(instance=movie)
    return render(request, 'editMovieDetails.html', {'movie':movie,'form':form})

def checkMovieDetails(request,slug):
  movie = newShow.objects.get(slug=slug)
  x=1

  if movie.screeningRoom==1:
    totalSeats = x*20
  else:
    totalSeats = x*30
  return render(request, 'checkMovieDetailscopy.html', {'movie':movie, 'totalSeats':range(totalSeats)})

def checkSeatDetails(request, seatCode, movie):

  return render(request, 'seatDetails.html', {'seatCode': seatCode})

# Screening Room 1 is 20 seats
# Screening Room 2 is 30 seats