from rest_framework import generics
from api.models import Transacao
from api.serializers import TransacaoSerializer

class TransacaoLista (generics.ListCreateAPIView):
  queryset = Transacao.objects.all()
  serializer_class = TransacaoSerializer