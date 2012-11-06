from django.contrib import admin
from models import Game, Event, Venue


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'submitter', 'when_from', 'approved',)
    list_filter = ('approved',)


class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'approved')
    list_filter = ('approved', 'city', )


admin.site.register(Game)
admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)