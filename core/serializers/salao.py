from rest_framework import serializers
from core.models import Salao, TelefoneSalao

class TelefoneSalaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneSalao
        fields = ['id', 'numero']

class SalaoSerializer(serializers.ModelSerializer):
    telefones = TelefoneSalaoSerializer(many=True, read_only=True)

    class Meta: 
        model = Salao
        fields = ['id', 'nome', 'endereco', 'telefones']