from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import ServicoAdicional

class ServicoRetriveSerializer(ModelSerializer):
    foto_servico = ImageSerializer(read_only=True)

    class Meta:
        model = ServicoAdicional
        fields = '__all__'

class ServicoSerializer(ModelSerializer):
    
    foto_attachment_key = SlugRelatedField(
        source='foto_servico',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = ServicoAdicional
        fields = '__all__'
    
