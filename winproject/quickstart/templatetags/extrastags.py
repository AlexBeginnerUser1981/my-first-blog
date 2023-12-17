from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    for kwarg in kwargs:
        try:
            print(query.urlencode())
            query.pop(kwarg)
        except KeyError:
            pass

    query.update(kwargs)

    return mark_safe(query.urlencode())

#-------вывод verbose name в шаблонах----------

@register.filter
def verbose_name(obj):
    return obj._meta.verbose_name


@register.filter
def verbose_name_plural(obj):
    return obj._meta.verbose_name_plural

"""add bellow code to template
{% load my_tags %}
{{ object|verbose_name }}
{{ object|verbose_name_plural }}
"""