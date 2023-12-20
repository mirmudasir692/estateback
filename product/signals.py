from .models import ProductImage, ProductVideo
from django.dispatch import receiver
from django.db.models.signals import post_delete


@receiver(post_delete, sender=ProductImage)
def DeleteImage(sender, instance, **kwargs):
    storage, path = instance.image.storage, instance.image.path
    if storage.exists(path):
        storage.delete(path)


@receiver(post_delete, sender=ProductVideo)
def DeleteImage(sender, instance, **kwargs):
    storage, path = instance.video.storage, instance.video.path
    if storage.exists(path):
        storage.delete(path)
        