from app.models import Todo, Cliente
from rest_framework import serializers

class Todo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 