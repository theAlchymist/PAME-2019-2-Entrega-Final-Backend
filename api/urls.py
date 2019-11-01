from django.urls import path
from api.views import *

urlpatterns = [
  path("users/", UserCreate.as_view(), name="user_create"),
]