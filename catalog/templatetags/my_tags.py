from django import template

register = template.Library()
@register.filter()
def media_filters(path):
    if path:
        return f'/media/{path}'
    return '#'