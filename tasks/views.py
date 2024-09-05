from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import  api_view
from rest_framework import status
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from tasks.models import Task
from tasks.serializers import TaskSerializer

# Create your views here.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def createTask(request):
    
    user = request.user
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response({"task": serializer.data}, status=status.HTTP_201_CREATED)
            
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getTask(request):  
    user = request.user
    tasks = Task.objects.filter(user=user)
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateTasksState(request):  
    user = request.user
    tasks_data = request.data.get('tasks', [])

    updated_tasks = []
    errors = []

    for task_data in tasks_data:
        task_id = task_data.get('id')
        completed = task_data.get('completed')

        if task_id is None or completed is None:
            errors.append({'id': task_id, 'error': 'Faltan datos en la solicitud'})
            continue

        try:
            task = Task.objects.get(id=task_id, user=user)
            serializer = TaskSerializer(task, data={'completed': completed}, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                updated_tasks.append(serializer.data)
            else:
                errors.append({'id': task_id, 'error': serializer.errors})
        
        except Task.DoesNotExist:
            errors.append({'id': task_id, 'error': 'Tarea no encontrada o no pertenece al usuario'})

    response_data = {
        'updated_tasks': updated_tasks,
        'errors': errors
    }
    
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def editTaskById(request,task_id):
    user = request.user
    try:
        task = Task.objects.get(id=task_id, user=user)
        data = request.data
        
        serializer = TaskSerializer(task, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"task": serializer.data}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Task.DoesNotExist:
        return Response({"error": "Tarea no encontrada."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteTaskById(request,task_id):
    user = request.user
    
    try:
        task = Task.objects.get(id=task_id, user=user)
        task.delete()
        
        return Response({"message": "Tarea eliminada correctamente."}, status=status.HTTP_204_NO_CONTENT)
    
    except Task.DoesNotExist:
        return Response({"error": "Tarea no encontrada."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteAllTasks(request):
    user = request.user
    
    deleted_count, _ = Task.objects.filter(user=user).delete()
    
    if deleted_count > 0:
        return Response({"message": f"{deleted_count} tareas eliminadas."}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"message": "No se encontraron tareas para eliminar."}, status=status.HTTP_404_NOT_FOUND)
