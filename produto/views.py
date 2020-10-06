from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from .models import Produto, Variacao

class ListaProdutos(ListView):
    model = Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 5

class DetalheProduto(DetailView):
    model = Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER',reverse('produto:lista'))
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(self.request,'Produto não existe')
            return render(http_referer)

        variacao = get_object_or_404(Variacao, id=variacao_id)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            # TODO: Variacao existe no carrinho
            pass
        else:
            # TODO: Variacao não existe no carrinho
            pass

        return HttpResponse('Adicionar ao Carrinho')

class RemoverDoCarrinho(View):
    pass

class Carrinho(View):
    pass
class Finalizar(View):
    pass


