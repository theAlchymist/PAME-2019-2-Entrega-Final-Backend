from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evento', default=1)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    inicio = models.DateTimeField()
    termino = models.DateTimeField()