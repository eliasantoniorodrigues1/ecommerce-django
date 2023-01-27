from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('lista')


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('detalhe')


class AdicionarAocarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('adicionaraocarrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('removerdocarrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('finalizar')
