# from core.models.decoracao import FotoDecoracao
# from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer, SlugRelatedField

# from uploader.models import Image
# from uploader.serializers import ImageSerializer

# from core.models import Decoracao

# class FotoDecoracaoSerializer(serializers.ModelSerializer):
#     imagem = ImageSerializer(read_only=True)
#     foto_decoracao_attachment_key = SlugRelatedField(
#         queryset=Image.objects.all(),
#         slug_field='attachment_key',
#         source='imagem'
#     )

#     class Meta:
#         model = FotoDecoracao
#         fields = ['id', 'imagem', 'foto_decoracao_attachment_key', 'decoracao']

# class DecoracaoSerializer(serializers.ModelSerializer):
#     fotos_decoracao = FotoDecoracaoSerializer(many=True, required=False)

#     class Meta:
#         model = Decoracao
#         fields = ['id', 'nome', 'descricao', 'fotos_decoracao', 'preco']