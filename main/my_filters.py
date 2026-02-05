from django import template

register = template.Library()

@register.filter
def inc(value):
    return value + 1