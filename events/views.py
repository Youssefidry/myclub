import json
from django.shortcuts import render , redirect
from .models import Event , Venue, Categories, Slider, info_event
from django.http import HttpResponse
from .forms import VenueForm , EventForm
# Create your views here.


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})


def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue.html', {'venue_list': venue_list})

def all_events(request):
    event_list = Event.objects.all()
    List_Categorie = Categories.objects.all()
    slider_items = Slider.objects.all()
    events = info_event.objects.all()
    return render(request, 'events/event_list.html', {'event_list': event_list, 'List_Categorie' : List_Categorie, 'events': events , 'slider_items': slider_items})

def home(request):
    slider_items = Slider.objects.all()
    events = info_event.objects.all()

    return render(request, 'events/home.html', {'slider_items': slider_items, 'events': events })

def add_venue(request):
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_venue?submitted=true')
    else:
        form = VenueForm()
    submitted = 'submitted' in request.GET
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})

def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/add_event?submitted=true')  # Redirect to the same page after successful form submission
    else:
        form = EventForm()
    submitted = 'submitted' in request.GET

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})

def slider_view(request):
    # Fetch all slider items from the database
    slider_items = Slider.objects.all()    
    # Pass the slider_items to the template for rendering
    return render(request, 'events/cover_slider.html', {'slider_items': slider_items})