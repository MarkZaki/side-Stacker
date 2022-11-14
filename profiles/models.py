from django.db import models
from django.contrib.auth.models import User
# token
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_toekn(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        profiles.objects.create(user=instance)
