from django import template
register = template.Library()

@register.filter(name='upper')
def upper(value):
  return value.upper()