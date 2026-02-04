from django.shortcuts import render
from user.models import User
from user.serializers import UserSerializer,RegisterUserSerializer
from rest_framework import viewsets

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer




class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=RegisterUserSerializer
