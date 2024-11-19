from rest_framework.decorators import api_view
from rest_framework import  viewsets

from app.models import  Cliente, Endereco, Pedido, Item, Vendedor, Forma_Pagamento
from app.serializers import  ClienteSerializer, EnderecoSerializer, PedidoSerializer, ItemSerializer, VendedorSerializer, Forma_PagamentoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer 

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer 


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer 

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer 

class Forma_PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Forma_Pagamento.objects.all()
    serializer_class = Forma_PagamentoSerializer 

