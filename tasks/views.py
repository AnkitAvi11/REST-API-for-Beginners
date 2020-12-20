from datetime import date, datetime

from django.db.models.query_utils import Q
from tasks.models import Task
from django.http import JsonResponse, HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from rest_framework.response import Response
from django.utils import timezone


#   for current day tasks (today's tasks)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def tasks(request) : 
    user = request.user
    
    tasks = Task.objects.filter(user=user, completion_date = datetime.now().date(), status=False).order_by('-completion_date')

    return Response(
        TaskSerializer(tasks, many=True).data,
        status=200
    )


#   for upcoming tasks (future tasks)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def upcomingTasks(request) : 
    user = request.user
    tasks = Task.objects.filter(
        user = user,
        completion_date__gt = datetime.now().date(),
        status = False
    )

    return Response(
        TaskSerializer(tasks, many=True).data,
        status=200
    )

#   for tasks which have been completed and not deleted
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def missedTasks(request) : 
    user = request.user
    tasks = Task.objects.filter(
        Q(user = user) & Q(status = False) & Q(completion_date__lt = datetime.now().date())
    )

    return Response(
        TaskSerializer(tasks, many=True).data,
        status=200
    )


#   function to complete the status of the task
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def completeTask(request, task_id) : 
    print("Task id = ", task_id)
    try : 
        task = Task.objects.get(id = task_id)
        task.status = True
        task.save()
        return Response({
            'message' : 'Saved successfully'
        })
    except Task.DoesNotExist :
        return Response({
            'error' : 'Task was not not found.'
        }, status=status.HTTP_404_NOT_FOUND)



#   function to add tasks
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def addtask(request) : 
    user = request.user
    title = request.POST.get('title')
    description = request.POST.get('description')
    date_ = request.POST.get('date')

    try : 
        Task.objects.create(
            user = user,
            title = title,
            completion_date = date_,
            description = description
        )
        return Response({
            'message' : 'task added successfully '
        },status=200)
    except : 
        return Response({
            'error' : 'Unexpected error occurred'
        }, status=status.HTTP_400_BAD_REQUEST)