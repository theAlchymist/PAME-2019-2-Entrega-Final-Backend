from rest_framework import generics
from api.models import Evento
from api.serializers import EventoSerializer

class EventoLista (generics.ListCreateAPIView):
  queryset = Evento.objects.all()
  serializer_class = EventoSerializer