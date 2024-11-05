from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Task

# Create your views here.


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request , pk):
    try:
        task = Task.objects.get(id = pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(task)
    return Response(serializer.data)












