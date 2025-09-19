from rest_framework import serializers
from core.models import Salao, TelefoneSalao, SalaoFotos
from uploader.models import Image
from uploader.serializers import ImageSerializer
from rest_framework.serializers import ModelSerializer, SlugRelatedField

class TelefoneSalaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneSalao
        fields = ['id', 'numero']

class SalaoFotosSerializer(serializers.ModelSerializer):
    imagem = ImageSerializer(read_only=True)
    foto_decoracao_attachment_key = SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        source='imagem'
    )

class SalaoSerializer(serializers.ModelSerializer):
    telefones = TelefoneSalaoSerializer(many=True, read_only=True)
    fotos = SalaoFotosSerializer(many=True, read_only=True)


    class Meta: 
        model = Salao
        fields = ['id', 'nome', 'endereco', 'telefones', 'fotos']
        