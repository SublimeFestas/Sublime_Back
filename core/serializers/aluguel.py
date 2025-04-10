from rest_framework import serializers
from core.models import Aluguel 

class AluguelSerializer(serializers.ModelSerializer):
    salao_nome = serializers.CharField(source='salao.nome', read_only=True)
    
    class Meta: 
        model = Aluguel
        fields = '__all__'
