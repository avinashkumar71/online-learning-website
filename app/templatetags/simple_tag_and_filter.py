from django import template
import math

register = template.Library()


@register.simple_tag
def percent(price, discount):
    sell_price = price
    if discount == 0 or discount is None:
        return sell_price
    sell_price = price - (price * (discount / 100))
    return math.floor(sell_price)


@register.filter(name='currency')
def currency(number):
    return '₹ ' + str(number)
