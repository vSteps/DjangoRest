from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.models import Todo
from app.serializers import Todo_Serializer

@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        serializer = Todo_Serializer(todo, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Todo_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_change_and_delete(request, pk):
    try:
        todo = Todo.objects.get(pk = pk)
    except Todo.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Todo_Serializer(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Todo_Serializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
