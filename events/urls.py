from django.urls import path
from . import views 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home" ),
    path('events', views.all_events, name="list-events"),
    path('add_venue', views.add_venue, name='add-venue'),
    path('add_event', views.add_event, name='add_event'),
    path('list_venues', views.list_venues, name="list-venues"),
    path('event_silders', views.slider_view, name="event-silders"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)