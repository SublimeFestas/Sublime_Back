from rest_framework import serializers
from core.models import Feedback, Aluguel

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'usuario', 'comentario', 'nota', 'criado_em']
        read_only_fields = ['usuario', 'criado_em']

    def validate(self, data):
        user = self.context['request'].user
        if not user or not user.is_authenticated:
            raise serializers.ValidationError("É necessário estar logado para enviar feedback.")
        return data
