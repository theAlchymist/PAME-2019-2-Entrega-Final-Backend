from rest_framework import generics
from api.serializers import UserSerializer

class UserCreate(generics.CreateAPIView):
  authentication_classes = ()
  permission_classes = ()
  serializer_class = UserSerializer
