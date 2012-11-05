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


@login_required
def add_event(request):
    new_event = EventForm()

    if request.method == 'POST':
        post_copy = request.POST.copy()
        new_event = EventForm(post_copy)
        if new_event.is_valid():
            new_event = new_event.save(commit=False)
            new_event.submitter = request.user
            new_event.save()
            return HttpResponseRedirect(reverse('index_games'))
        else:
            print new_event.errors

    params = {
        'new_event': new_event
    }
    return render_to_response('events/add.html', params,
        context_instance=RequestContext(request))

@login_required
def index(request):
    params = {
        'events': Event.objects.all()
    }
    return render_to_response('games/index.html', params,
        context_instance=RequestContext(request))