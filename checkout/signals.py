from django.db.models.signals import post_save, post_delete
from django.dispatch import reciever

from .models import OrderLineItem 

@reciever(post_save, sender = OrderLineItem)
def update_on_save (sender, instance, created, **kwargs):
    """ Update subtotal when item updated """
    instance.order.update_total()

@reciever(post_delete, sender = OrderLineItem)
def update_on_delete (sender, instance, **kwargs):
    """ Update subtotal when item deleted """
    instance.order.update_total()