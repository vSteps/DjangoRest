from app.models import * #type: ignore
from rest_framework import serializers #type: ignore
from django.contrib.auth.models import User #type: ignore

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'perfil', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = usuario.objects.create_usuario(**validated_data)
        return usuario

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['cpf', 'usuario']           
        extra_kwargs = {'password': {'write_only': True}}

    usuario = UsuarioSerializer()
    

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_serializer = UsuarioSerializer(data=usuario_data)      
        usuario_serializer.is_valid(raise_exception=True)

        usuario = usuario_serializer.save()

        cliente = Cliente.objects.create(usuario=usuario, **validated_data)
        return cliente


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['cpf', 'usuario']           
        extra_kwargs = {'password': {'write_only': True}}

    usuario = UsuarioSerializer()
    

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_serializer = UsuarioSerializer(data=usuario_data)      
        usuario_serializer.is_valid(raise_exception=True)

        usuario = usuario_serializer.save()

        vendedor = Vendedor.objects.create(usuario=usuario, **validated_data)
        return vendedor
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__' 

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__' 

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' 

class Forma_PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forma_Pagamento
        fields = '__all__' 