from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, UserprofileSerializer
from rest_framework.response import Response
from .validators import isemail, isvalid_password, isvalid_username
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.authentication import TokenAuthentication


#   method to register a new user into the application
@csrf_exempt
@api_view(['POST'])
def signupUser(request) : 
    if request.method == 'POST' : 
        username = request.data.get('username')
        fname = request.data.get('fname')
        fname = fname.split(" ", 1)
    
        last_name = fname[1] if len(fname) > 1 else ""
        first_name = fname[0]
        email = request.data.get('email')
        password = request.data.get('password')

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
@csrf_exempt
@api_view(['POST'])
def loginUser(request) : 

    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)

    if user is None : 
        return Response({
            'error' : 'Invalid username or password'
        }, status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user = user)

    login(request, user)

    return Response({
        "user" : UserprofileSerializer(user).data,
        "token" : token.key
    }, status=200)


#   method to log the user out from the application
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logoutUser(request) : 
    logout(request)
    return Response({
        'message' : 'Succesfully logged out.'
    })


#   api to get the current user information
@api_view(['GET'])
def getUser(request) : 
    username = request.GET.get('username')

    try : 
        user = User.objects.get(username=username)
        return Response(UserprofileSerializer(user).data)
    except User.DoesNotExist : 
        return Response({'error' : 'User does not exist'}, status=404)


#   to check if the token is valid or not 
@api_view(['GET'])
def validateUser(request) : 
    token = request.GET.get('token')
    if token is not None : 
        try : 
            token = Token.objects.get(key=token)
            user = token.user
            return Response(UserprofileSerializer(user).data, status=200)
        except Token.DoesNotExist: 
            return Response({
                'error' : 'User does not exist'
            }, status=404)
    else : 
        return Response({
            'error' : 'Invalid token'
        })


#   method to update the user when authenticated
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@csrf_exempt
def updateUser(request) : 
    user = request.user
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email = request.POST.get('email')

    try : 
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()

        return Response(
            UserSerializer(user).data,
            status=200
        )

    except Exception as e : 
        return Response({
            'error' : str(e)
        }, status=400)


#   api view to change the password of a user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@csrf_exempt
def updatePassword(request) : 
    username = request.user.username
    old_password = request.POST.get('password')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if password1 != password2 : 
        return Response({
            'error' : 'Invalid password entered'
        }, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    user = authenticate(username=username, password=old_password)

    

