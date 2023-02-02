from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from . import models
from django.contrib import messages


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AdicionarAocarrinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
            )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(self.request, 'Produto não existe.')
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.requet.session.save()

        carrinho = self.requet.session['carrinho']

        if variacao_id in carrinho:
            # TODO: Variação existe no carrinho
            pass
        else:
            # checar se o estoque da variação é o suficiente para adicionar
            # no carrinho.
            # TODO: Variação não existe no carrinho
            pass

        return HttpResponse(f'{variacao.produto} {variacao.nome}')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('removerdocarrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('finalizar')
