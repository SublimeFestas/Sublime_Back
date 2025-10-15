from rest_framework import serializers
from core.models import User, TelefoneUsuario

class TelefoneUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneUsuario
        fields = ['id', 'numero']

class UserSerializer(serializers.ModelSerializer):
    telefones = TelefoneUsuarioSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'telefones']