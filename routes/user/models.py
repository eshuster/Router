from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from athlete.models import Athlete

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
        if created:
            if not instance.is_staff or not instance.is_superuser:
                UserProfile.objects.create(user=instance)
                Athlete.objects.create(user=instance)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


