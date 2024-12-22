from django import template

register = template.Library()

@register.filter
def slider_filter(services, pk):
    return services.filter(pk=pk)