from django.db.models.signals import pre_save
from django.dispatch import receiver

from youngun.apps.usermanager.models import Profile
from .models import User


@receiver(pre_save, sender=User)
def create_related_profile(sender, instance, *args, **kwargs):
    if not instance.profile:
        new_profile, created = Profile.objects.get_or_create(user=instance)
        if created:
            new_profile.save()

        instance.profile = new_profile
