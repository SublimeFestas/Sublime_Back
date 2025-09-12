from rest_framework.viewsets  import ModelViewSet

from core.models import ServicoAdicional
from core.serializers import ServicoSerializer

class ServicoViewset(ModelViewSet):
    queryset = ServicoAdicional.objects.all()
    serializer_class = ServicoSerializer