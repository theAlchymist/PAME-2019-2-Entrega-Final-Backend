from django.db import models
from django.utils import timezone

class Funcionario (models.Model):
  # Atributos
  email = models.EmailField(max_length=254)
  senha = models.CharField(max_length=20)
  nome = models.CharField(max_length=254)
  # foto = models.ImageField()
  cpf = models.BigIntegerField()
  # sexo =
  # turno = 
  # nascimento = 
  admissão = models.DateTimeField(default=timezone.now)
  cargo = models.CharField(max_length=20)
  salario = models.IntegerField()

  # Relacionamentos