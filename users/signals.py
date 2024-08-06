from django.dispatch import receiver
from django.db.models.signals import post_save
from orders.models import Cart
from users.models import User

@receiver(post_save,sender=User)
def cart_signal(sender,instance,created,**kwargs):
    if created:
        Cart.objects.create(user=instance)
