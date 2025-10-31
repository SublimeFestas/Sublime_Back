from rest_framework import serializers
from core.models import Feedback, Aluguel

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'comentario', 'nota', 'criado_em']
        read_only_fields = ['usuario', 'criado_em']
