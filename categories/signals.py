from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Category


@receiver(post_delete, sender=Category)
def DeleteTheCategory(sender, instance, **kwargs):
    storage, path = instance.image.storage, instance.image.path
    if storage.exists(path):
        storage.delete(path)

