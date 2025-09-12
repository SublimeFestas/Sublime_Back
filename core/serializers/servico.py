from rest_framework.serializers import ModelSerializer

from core.models import ServicoAdicional

class ServicoSerializer(ModelSerializer):
    class Meta:
        model = ServicoAdicional
        fields = '__all__'
    
