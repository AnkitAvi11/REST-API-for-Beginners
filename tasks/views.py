from tasks.models import Task
from django.http import JsonResponse, HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from rest_framework.response import Response
from django.utils import timezone

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def tasks(request) : 
    user = request.user

    tasks = Task.objects.filter(user=user, completion_date = timezone.now().date(), status=False).order_by('-completion_date')

    return Response(
        TaskSerializer(tasks, many=True).data,
        status=200
    )
