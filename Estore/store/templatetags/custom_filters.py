from django import template
from store.models import Cart,OrderItem
from django.contrib.auth.models import User

register = template.Library()
@register.filter(name="cart_count")
def cart_count_filter(value):
    return Cart.objects.filter(customer__id=value).count() 

@register.filter(name="ordered_count")
def ordered_count_filter(value):
    return OrderItem.objects.filter(order__customer__id=value).count()