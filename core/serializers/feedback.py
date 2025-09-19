from rest_framework import serializers
from core.models import Feedback, Aluguel

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'usuario', 'salao', 'comentario', 'nota', 'criado_em']
        read_only_fields = ['usuario', 'criado_em']

    def validate(self, data):
        user = self.context['request'].user
        salao = data['salao']
        if not user or not user.is_authenticated:
            raise serializers.ValidationError("É necessário estar logado para enviar feedback.")
        if not Aluguel.objects.filter(usuario=user, salao=salao).exists():
            raise serializers.ValidationError("Você só pode avaliar salões que já alugou.")
        return data
