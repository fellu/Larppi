from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    twitter_id = models.IntegerField(null=True, blank=True)
    profile_complete = models.BooleanField(default=True)
    flair = models.CharField(max_length=80, default="new")
    favorite_animal = models.CharField(max_length=20, default="Dragons.")


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)


