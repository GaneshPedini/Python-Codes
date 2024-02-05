from django import template

register = template.Library()

@register.filter
def in_category(product, category):
    return product.filter(category=category)