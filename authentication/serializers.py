from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Userprofile

class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class LoginUserSerialiser(serializers.ModelSerializer) :
    class Meta : 
        model = Userprofile
        fields = [
            'id',
            'bio',
            'profile_pic',
            'joined_on',
        ]

class UserprofileSerializer(serializers.ModelSerializer) : 
    
    userprofile = LoginUserSerialiser(many=False, read_only=False)

    class Meta : 
        model = User

        fields = [
            'id',
            'username',
            'email',
            'userprofile'
        ]