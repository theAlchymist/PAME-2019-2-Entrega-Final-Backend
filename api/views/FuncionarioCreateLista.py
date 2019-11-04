from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import User, Funcionario
from api.serializers import FuncionarioSerializer
from django.shortcuts import get_object_or_404, get_list_or_404

class FuncionarioCreateLista(APIView):
    def get(self, request):
      lista = get_list_or_404(Funcionario)
      data = FuncionarioSerializer(lista, many = True).data
      return Response(data)

    def post(self, request):
      # Busca User no DB
      user = get_object_or_404(User, username=request.data['username'])

      # Instancia o Funcionario
      funcionario = Funcionario(
        user = user,
        is_admin = request.data['is_admin'],

        nome = request.data['nome'],
        sexo = request.data['sexo'],
        data_nascimento = request.data['data_nascimento'],
        naturalidade = request.data['naturalidade'],
        nacionalidade = request.data['nacionalidade'],
        estado_civil = request.data['estado_civil'],
        endereco = request.data['endereco'],
        telefone = request.data['telefone'],
        celular = request.data['celular'],

        rg = request.data['rg'],
        cpf = request.data['cpf'],
        ctps = request.data['ctps'],
        pis_pasep = request.data['pis_pasep'],
        titulo_eleitoral = request.data['titulo_eleitoral'],
        certificado_reservista = request.data['certificado_reservista'],
      
        data_admissao = request.data['data_admissao'],
        cargo = request.data['cargo'],
        turno = request.data['turno'],
        salario = request.data['salario'],
        ferias = request.data['ferias'],
        acidentes_doencas = request.data['acidentes_doencas'],
        encargos_sociais = request.data['encargos_sociais'],
        filiacao = request.data['filiacao']
      )

      # Salva no DB
      funcionario.save()
      # Serializa
      data = FuncionarioSerializer(funcionario).data
      # Devolve pro Front
      return Response(data)