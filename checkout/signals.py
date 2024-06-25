from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

def update_on_save(send, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """

    instance.order.update_total()