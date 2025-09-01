from rest_framework import serializers
from core.models import Aluguel, User

class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'phone']

class AluguelSerializer(serializers.ModelSerializer):
    salao_nome = serializers.CharField(source='salao.nome', read_only=True)
    user = UserBaseSerializer(read_only=True)

    class Meta: 
        model = Aluguel
        fields = '__all__'
