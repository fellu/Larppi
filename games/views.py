from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from forms import EventForm, VenueForm
from models import Event


@login_required()
def add_venue(request):
    new_venue = VenueForm()

    if request.method == 'POST':
        post_copy = request.POST.copy()
        new_venue = VenueForm(post_copy)
        if new_venue.is_valid():
            new_venue = new_venue.save(commit=False)
            new_venue.submitter = request.user
            new_venue.save()
            return HttpResponseRedirect(reverse('index_games'))
        else:
            print new_venue.errors

    params = {
        'new_venue': new_venue
    }


    return render_to_response('venues/add.html', params,
        context_instance=RequestContext(request))


def add_event(request):
    """
    Creates new event and venue from POST request
    """
    new_event = EventForm()
    new_venue = VenueForm()

    if request.method == 'POST':
        new_event = EventForm(request.POST)
        new_venue = VenueForm(request.POST)

        # If event and venue form vas valid
        if new_event.is_valid() and new_venue.is_valid:
            new_venue = new_venue.save()
            new_event = new_event.save(commit=False)
            new_event.where = new_venue

            # Check for authenticated user
            if request.user.is_authenticated:
                new_event.submitter = request.user # Add authenticated as event submitter
            try:
                new_event.save()
            except Exception as e:
                new_venue.delete() # Remove added venue if event saving fails
                raise
        return HttpResponseRedirect(reverse('index_games'))

    params = {
        'new_event': new_event, 'new_venue': new_venue
    }
    return render_to_response('events/add.html', params,
        context_instance=RequestContext(request))

@login_required
def index(request):
    params = {
        'events': Event.objects.filter(approved=True)
    }
    return render_to_response('games/index.html', params,
        context_instance=RequestContext(request))


