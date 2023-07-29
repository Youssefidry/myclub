from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    N_categorie = models.CharField(max_length=100)

    def __str__(self):
        return self.N_categorie

class Speakers(models.Model):
    N_Speakers = models.CharField(max_length=25)
    N_Categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.N_Speakers

class Venue(models.Model):
    name = models.CharField(max_length=100, verbose_name='Venue Name')
    address = models.CharField(max_length=200)
    website = models.URLField(max_length=200)  # Use URLField for storing website URLs
    zip_code = models.CharField(max_length=10, verbose_name='ZIP Code')
    phone = models.CharField(max_length=20, verbose_name='Contact Phone')
    email_address = models.EmailField(max_length=100, verbose_name='Email Address')

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    email = models.EmailField(max_length=100, verbose_name='Email')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Event(models.Model):
    name = models.CharField(max_length=120, verbose_name='Event Name')
    event_date = models.DateField(verbose_name='Event Date')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)  # ForeignKey relationship with Categories model
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True , null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    speakers = models.ForeignKey(Speakers, blank=True, null=True, on_delete=models.CASCADE)



    def __str__(self):
        return self.name

class Slider(models.Model):
    background_image = models.ImageField(upload_to='slider_images')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    date_text = models.CharField(max_length=50)
    button_text = models.CharField(max_length=50)
    button_link = models.URLField()

    def __str__(self):
        return self.title


class info_event(models.Model):
    ICON_CHOICES = [
        ('ion-ios-calendar-outline', 'DATE'),
        ('ion-ios-location-outline', 'location'),
        ('ion-ios-person-outline', 'speakers'),
        ('ion-ios-pricetag-outline', 'tickets'),
    ]

    title = models.CharField(max_length=100, choices=ICON_CHOICES)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}: {self.content}"