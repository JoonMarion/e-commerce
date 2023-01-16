from django.urls import path
from .views import *

app_name = 'lojaapp'

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("sobre/", SobreView.as_view(), name='sobre'),
    path("contato/", ContatoView.as_view(), name='contato'),

    path("produtos/", TodosProdutosView.as_view(), name='produtos'),
    path("produto/<slug:slug>/", ProdutoDetalheView.as_view(), name='produtodetalhe'),

    path("addcarro-<int:pro_id>/", AddCarroView.as_view(), name='addcarro'),
    path("meucarro/", MeuCarroView.as_view(), name='meucarro'),
    path("manipular-carro/<int:cp_id>/", ManipularCarroView.as_view(), name='manipularcarro'),
    path("limpar-carro/", LimparCarroView.as_view(), name='limparcarro'),
    path("checkout/", CheckoutView.as_view(), name='checkout'),

    path("registrar/", ClienteRegistrarView.as_view(), name='clienteregistrar'),
]