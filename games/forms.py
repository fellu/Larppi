from django.forms import ModelForm
from models import Event, Venue

class EventForm(ModelForm):
    class Meta:
        model = Event


class VenueForm(ModelForm):
    class Meta:
        model = Venue
