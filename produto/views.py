from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from .models import Produto

class ListaProdutos(ListView):
    model = Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 5

class DetalheProduto(View):
    pass

class AdicionarAoCarrinho(View):
    pass

class RemoverDoCarrinho(View):
    pass

class Carrinho(View):
    pass
class Finalizar(View):
    pass


