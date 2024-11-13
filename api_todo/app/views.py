from rest_framework.decorators import api_view
from rest_framework import  viewsets

from app.models import  Cliente, Endereco
from app.serializers import  ClienteSerializer, EnderecoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer 