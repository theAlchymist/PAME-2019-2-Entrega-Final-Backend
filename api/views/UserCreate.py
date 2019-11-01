from django.shortcuts import render
from rest_framework import generics
from api.serializers import UserSerializer

class UserCreate(generics.CreateAPIView):
  serializer_class = UserSerializer