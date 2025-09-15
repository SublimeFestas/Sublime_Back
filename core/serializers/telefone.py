from rest_framework import serializers
from core.models import User, TelefoneUsuario, Salao, TelefoneSalao

class TelefoneUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneUsuario
        fields = ['id', 'numero']

class UserSerializer(serializers.ModelSerializer):
    telefones = TelefoneUsuarioSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'phone', 'telefones']

class TelefoneSalaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneSalao
        fields = ['id', 'numero']

class SalaoSerializer(serializers.ModelSerializer):
    telefones = TelefoneSalaoSerializer(many=True, read_only=True)

    class Meta:
        model = Salao
        fields = ['id', 'nome', 'endereco', 'telefones']