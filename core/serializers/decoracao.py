from rest_framework import serializers
from core.models import Decoracao

class DecoracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decoracao
        fields = '__all__'