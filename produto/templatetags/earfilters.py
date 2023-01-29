from django.template import Library
from utils import util

register = Library()


@register.filter
def formata_preco(valor):
    return util.formata_preco(valor)
