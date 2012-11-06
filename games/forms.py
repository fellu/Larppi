from django.forms import ModelForm
from models import Event, Venue

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('where', 'approved', )



class VenueForm(ModelForm):
    class Meta:
        model = Venue
        exclude = ('approved', )
