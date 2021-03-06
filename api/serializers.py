from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}
  
  def create(self, validated_data):
    user = User(
      email=validated_data['email'],
      username=validated_data['username']
    )
    user.set_password(validated_data['password'])
    user.save()
    Token.objects.create(user=user)
    return user

class EventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Evento
    fields  = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Funcionario
    fields  = '__all__'

class TransacaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transacao
    fields  = '__all__'