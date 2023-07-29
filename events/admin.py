from django.contrib import admin
from .models import Venue, MyClubUser, Event, Categories, Speakers,Slider, info_event
# Register your models here.

#admin.site.register(Venue)
admin.site.register(MyClubUser)
#admin.site.register(Event)
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address', )

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description','manager', 'categories', 'speakers')
    list_display = ('name', 'event_date', 'venue', 'categories')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('N_categorie',)

@admin.register(Speakers)
class SpeakersAdmin(admin.ModelAdmin):
    list_display = ('N_Speakers', 'N_Categorie',) 


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_text')
    fieldsets = (
        ('Slider Information', {
            'fields': ('background_image', 'title', 'subtitle', 'date_text', 'button_text', 'button_link')
        }),
    )

@admin.register(info_event)
class EventInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')