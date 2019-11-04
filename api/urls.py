from django.urls import path
from api.views import *
from rest_framework.authtoken import views # Adicionado, já existe no DRF

# O Endpoint se baseia em por a requisicao que o front deseja, a view que o endpoint utiliza e o name foi copiado.

urlpatterns = [
  path("users/", UserCreate.as_view(), name="user_create"),
  path("login/", views.obtain_auth_token, name="login"),
  path("calendario/", EventoLista.as_view(), name="calendario"),
  path("funcionario/", FuncionarioCreateLista.as_view(), name="funcionario_create_lista"),
  path("busca-funcionario/", FuncionarioBusca.as_view(), name="funcionario_busca")
]