from django import template
from datetime import datetime
register = template.Library()

@register.filter(name='attr')
def attr(obj, attr_name):
    return getattr(obj, attr_name, '')

@register.filter(name='convert_date_format')
def convert_date_format(value):
    return value.strftime("%Y-%m-%d")

@register.filter
def get_item(lst, i):
    try:
        return lst[i]
    except (IndexError, TypeError):
        return None

@register.simple_tag
def custom_sort(obj, sort, param):
    if param == 0:
        if sort == "desc":
            return obj.order_by("-uploaded_at")
        elif sort == "asc":
            return obj.order_by("uploaded_at")
    if sort == "desc":
        return obj.order_by(f"-{param}")
    elif sort == "asc":
        return obj.order_by(param)
    return obj

@register.simple_tag
def getIndex(obj, obj2, key):
    for index, el in enumerate(obj2):
        if el == key:
            return obj[index]
    return 0