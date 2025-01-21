## Permissions
from rest_framework.decorators import authentication_classes, permission_classes # type: ignore
from rest_framework.permissions import IsAuthenticated  # type: ignore
from rest_framework.authentication import TokenAuthentication, SessionAuthentication # type: ignore
from django.shortcuts import get_object_or_404 # type: ignore


from rest_framework.decorators import api_view # type: ignore
from rest_framework import  viewsets # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status  # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from rest_framework.authentication import BasicAuthentication # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User # type: ignore
from rest_framework.authtoken.models import Token # type: ignore

from app.models import  * # type: ignore
from app.serializers import * # type: ignore

class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUsuarioView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            token, created = Token.objects.get_or_create(user=usuario)
            if created:
                token.delete()  
                token = Token.objects.create(user=usuario)
            return Response({'token': token.key, 'username': usuario.username, 'perfil': usuario.perfil})
        else:
            return Response({'mensagem': 'Login ou Senha Inválido'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutUsuarioView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.headers) 
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()

        return Response({'detail': 'Usuário deslogado com sucesso.'})

class ClienteRegistrationView(APIView):
    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            token, created = Token.objects.get_or_create(user=usuario)
            if created:
                token.delete()  
                token = Token.objects.create(user=usuario)

            response_data = {
                'token': token.key,
                'username': usuario.username,
                'perfil': user.perfil,
            }

            if usuario.perfil == 'cliente':
                cliente = usuario.cliente 
                if cliente is not None:
                    cliente_data = ClienteSerializer(cliente).data
                    response_data['data'] = cliente_data

            return Response(response_data)
        else:
            return Response({'message': 'Usuário ou Senha Inválido'}, status=status.HTTP_401_UNAUTHORIZED)

class VendedorRegistrationView(APIView):
    def post(self, request):
        serializer = VendedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendedorLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            token, created = Token.objects.get_or_create(user=usuario)
            if created:
                token.delete() 
                token = Token.objects.create(user=usuario)

            response_data = {
                'token': token.key,
                'username': usuario.username,
                'perfil': usuario.perfil,
            }

            if usuario.perfil == 'vendedor':
                vendedor = usuario.vendedor  
                if vendedor is not None:
                    vendedor_data = VendedorSerializer(vendedor).data
                    response_data['data'] = vendedor_data

            return Response(response_data)
        else:
            return Response({'message': 'Usuário ou Senha Inválido'}, status=status.HTTP_401_UNAUTHORIZED)

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer 

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer 


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer 

class Forma_PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Forma_Pagamento.objects.all()
    serializer_class = Forma_PagamentoSerializer 

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer 
