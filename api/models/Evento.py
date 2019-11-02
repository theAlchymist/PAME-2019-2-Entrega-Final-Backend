from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    inicio = models.DateTimeField()
    termino = models.DateTimeField()