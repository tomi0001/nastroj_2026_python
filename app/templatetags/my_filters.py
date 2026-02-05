from django import template
register = template.Library()

class Counter:
    def __init__(self, start=1):
        self.value = start

    def inc(self, step=1):
        self.value += step
        return self.value

    def get(self):
        return self.value


@register.simple_tag
def make_counter(start=1):
    return Counter(start)

@register.simple_tag
def next(counter, step=1):
    return counter.inc(step)

@register.simple_tag
def get_counter(counter):
    return counter.get()