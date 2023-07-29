from django import forms
from django.forms import ModelForm
from .models import Venue , Event,Categories, Speakers, info_event

# create a venue form

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'email_address')
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'web': forms.TextInput(attrs={'class':'form-control','placeholder':'Website Address'}),
            'email_address': forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name','event_date', 'venue', 'manager', 'description', 'attendees', 'categories','speakers')
        labels = {
            'name' : '',
            'event_date' : '',
            'venue' : '',
            'manager' : '',
            'description' : '',
            'attendees' : '',
            'categories' : '',
            'speakers' : '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'venue': forms.Select(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'speakers': forms.Select(attrs={'class': 'form-control'}),
        }
class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['N_categorie']

class SpeakersForm(forms.ModelForm):
    class Meta:
        model = Speakers
        fields = ['N_Speakers', 'N_Categorie']  # Correct field name is 'Categorie'
        labels = {
            'N_Speakers': '',  # Corrected the label for 'N_Speakers'
            'N_Categorie': '',  # Corrected the label for 'Categorie'
        }


class EventInfoForm(forms.ModelForm):
    class Meta:
        model = info_event
        fields = ('title', 'content')