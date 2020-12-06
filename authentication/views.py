from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.response import Response
from .validators import isemail, isvalid_password, isvalid_username
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login, logout
from rest_framework import status

@api_view(['POST'])
@csrf_exempt
def signupUser(request) : 
    if request.method == 'POST' : 
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        fname = fname.split(" ")
    
        last_name = fname[1] if len(fname) > 1 else ""
        first_name = fname[0]
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not isemail(email) : 
            return Response({
                'error' : 'Invalid email address'
            }, status=400)

        if not isvalid_username(username) : 
            return Response({'error' : 'Invalid username', 'message' : 'username must be greater than 8 characters'}, status=400)
        
        if not isvalid_password(first_name, password) : 
            return Response({'error' : 'Password must not contain your username and must be greater than 8 characters'})

        if User.objects.filter(Q(username=username) | Q(email=email)).exists() : 
            return Response({'error' : 'User with that username or email already exists'}, status=400)
        else : 
            try : 
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    first_name = first_name,
                    last_name = last_name,
                    password = password
                )
                return Response(
                    UserSerializer(user).data,
                    status=200
                )
            except : 
                return Response({
                    'error' : "Bad request"
                }, status=400)

    else : 
        return Response({'error' : 'Bad request method'}, status=400)



#   method to login a user into the application
@api_view(['POST'])
def loginUser(request) : 
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is None : 
        return Response({
            'error' : 'Invalid username or password'
        }, status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)

    login(request, user)

    return Response({
        "user" : UserSerializer(user).data,
        "token" : token.key
    }, status=200)