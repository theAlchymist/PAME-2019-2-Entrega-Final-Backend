from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Funcionario
from api.serializers import FuncionarioSerializer
from django.shortcuts import get_list_or_404

class FuncionarioBusca(APIView):
    def get(self, request):
      lista_busca = get_list_or_404(Funcionario)
      lista_resultado = []
      lista_filtros = request.data.values()
      # Varre a lista de filstros inseridos
      for filtro in lista_filtros:
        # Varre a ficha de funcionarios
        for funcionario in lista_busca:
          funcionario_values = funcionario.__dict__.values()
          # Varre os dados da ficha do funcionario
          for valor in funcionario_values:
            # Se não foi inserido um dado no filtro, passe
            if valor == "":
              continue
            # Compara o dado do funcionario com o do filtro
            elif valor == filtro:
              lista_resultado.append(funcionario)
              break
      data = FuncionarioSerializer(lista_resultado, many = True).data
      return Response(data)