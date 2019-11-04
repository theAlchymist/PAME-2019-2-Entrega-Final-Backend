from django.db import models
from django.contrib.auth.models import User

# Existem alguns dados que aparecem como obrigatorios em fichas de admissao, conforme o artigo 41 da Lei da CLT

class Funcionario(models.Model):
  # Informações de Cadastro
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='funcionario')
  is_admin = models.BooleanField(default=False)
  join_date = models.DateTimeField(auto_now=True) # Não precisa importar o timezone

  # Informações Pessoais
  nome = models.CharField(max_length=30)
  sexo = models.CharField(max_length=1)
  data_nascimento = models.DateTimeField()
  naturalidade = models.CharField(max_length=30, default="Rio de Janeiro - RJ")
  nacionalidade = models.CharField(max_length=20, default="Brasil")
  estado_civil = models.CharField(max_length=10, default="Solteiro(a)")
  endereco = models.TextField()
  telefone = models.CharField(max_length=20)
  celular = models.CharField(max_length=20)

  # Documentos
  rg = models.CharField(max_length=12)
  cpf = models.CharField(max_length=14)
  ctps = models.CharField(max_length=12)
  pis_pasep = models.CharField(max_length=14)
  titulo_eleitoral = models.CharField(max_length=14)
  certificado_reservista = models.CharField(max_length=12)
  
  # Informações de Trabalho
  data_admissao = models.DateTimeField()
  cargo = models.CharField(max_length=20)
  turno = models.CharField(max_length=10)
  salario = models.CharField(max_length=20)
  ferias = models.TextField(default="Não definido")
  acidentes_doencas = models.TextField(default="Não possui")
  encargos_sociais = models.TextField(default="Não possui")
  filiacao = models.CharField(max_length=20, default="Não possui")

  def __str__(self):
    return self.nome