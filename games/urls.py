from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^games/?$', 'games.views.index', name="games"),
    url(r'^games/index/?$', 'games.views.index', name="index_games"),
    url(r'^events/add/?$', 'games.views.add_event', name="add_event"),
    url(r'^venues/add/?$', 'games.views.add_venue', name="add_venue"),
)