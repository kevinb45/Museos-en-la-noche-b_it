from django import template
from museos.models import Museo

register = template.Library()

@register.simple_tag
def get_museo_list():
    museos = Museo.objects.all()
    return museos