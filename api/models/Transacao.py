from django.db import models
from django.contrib.auth.models import User

class Transacao(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transacao')
  descricao = models.CharField(max_length=30, default='Não definida')
  tipo = models.CharField(max_length=10)
  valor = models.CharField(max_length=20)
  data = models.DateTimeField(auto_now=True)