from rest_framework import serializers
from core.models import User, TelefoneUsuario


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class TelefoneUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneUsuario
        fields = ['numero']

class UserSerializer(serializers.ModelSerializer):
    telefones = TelefoneUsuarioSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'telefones']
