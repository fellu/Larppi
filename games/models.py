# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    hosts = models.ManyToManyField(User, related_name="hosts", verbose_name=u"Pelinjohto")
    players = models.ManyToManyField(User, related_name="players", blank=True, null=True, verbose_name=u"Pelaajat")
    rules = models.TextField(verbose_name=u"Säännöt")


class Venue(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Nimi")
    city = models.CharField(max_length=255, verbose_name=u"Kaupunki")
    address = models.CharField(blank=True, null=True, max_length=255, verbose_name=u"Osoite")
    description = models.TextField(blank=True, null=True, verbose_name=u"Kuvaus")

    def __unicode__(self):
        return self.name


class Event(models.Model):
    submitter = models.ForeignKey(User, editable=False, verbose_name=u"Lisääjä")
    title = models.CharField(max_length=100, verbose_name=u"Pelin nimi")
    details = models.TextField(verbose_name=u"Lisätietoja")
    when_from = models.DateTimeField(blank=True, null=True, verbose_name=u"Mistä")
    when_to = models.DateTimeField(blank=True, null=True, verbose_name=u"Mihin")
    where = models.ForeignKey(Venue, verbose_name=u"Pelipaikka")
    fee = models.IntegerField(blank=True, null=True, verbose_name=u"Pelimaksu")  # Pelimaksu
    game = models.ForeignKey(Game, editable=False, blank=True, null=True, verbose_name=u"Peli")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-when_from']

    def __unicode__(self):
        return self.title
