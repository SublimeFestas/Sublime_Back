from rest_framework import serializers
from core.models import Aluguel, User, ServicoAdicional

class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']

class ServicoAdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoAdicional
        fields = ['id', 'nomeServico', 'valor']

class AluguelSerializer(serializers.ModelSerializer):
    user = UserBaseSerializer(read_only=True)
    servico = ServicoAdicionalSerializer(many=True, read_only=True)

    # campo apenas para entrada
    servico_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Aluguel
        fields = '__all__'
        read_only_fields = ['user', 'servico']

    def create(self, validated_data):
        servico_ids = validated_data.pop('servico_ids', [])
        user = self.context['request'].user

        aluguel = Aluguel.objects.create(user=user, **validated_data)

        if servico_ids:
            aluguel.servico.set(servico_ids)

        return aluguel