from django.template import Library
from utils import util

register = Library()


@register.filter
def formata_preco(valor):
    return util.formata_preco(valor)


@register.filter
def cart_total_qtd(carrinho):
    return util.cart_total_qtd(carrinho)


@register.filter
def cart_totals(carrinho):
    return util.cart_totals(carrinho)

