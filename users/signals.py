from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# here we are creating a user profile for each new user automatically
@receiver(post_save, sender=User)  # this is saying that when a user is saved send this signal to receiver
def create_profile(sender, instance, created, **kwargs):  # this function is the create profile function receiver
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
