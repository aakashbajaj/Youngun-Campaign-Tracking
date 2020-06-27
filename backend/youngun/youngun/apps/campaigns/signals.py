from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Campaign


@receiver(pre_save, sender=Campaign)
def slugify_campaign_if_not_exists(sender, instance, *args, **kwargs):
    if instance:
        slug = slugify(instance.brand.name + "-" + instance.name)
        instance.slug = slug
