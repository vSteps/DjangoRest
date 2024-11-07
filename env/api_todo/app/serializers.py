from app.models import Todo
from rest_framework import serializers

class Todo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"