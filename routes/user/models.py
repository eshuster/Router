from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from enum import IntEnum

class Profile(models.Model):

    class ProfileTypes(IntEnum):
        ADMIN = 1
        USER = 2

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_type_choices = [(key.value, key.name) for key in ProfileTypes]

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField(choices=profile_type_choices, default=ProfileTypes.USER)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            if instance.is_staff or instance.is_superuser:
                Profile.objects.create(user=instance, type=1)
            else:
                Profile.objects.create(user=instance, type=2)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class UserProfile(Profile):
    pass
