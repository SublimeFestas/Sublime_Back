from rest_framework.viewsets import ModelViewSet

from core.models import Decoracao
from core.serializers import DecoracaoSerializer

class DecoracaoViewSet(ModelViewSet):
    queryset = Decoracao.objects.all()
    serializer_class = DecoracaoSerializer