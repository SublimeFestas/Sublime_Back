from rest_framework.viewsets import ModelViewSet

from core.models import Aluguel
from core.serializers.aluguel import AluguelSerializer

class AluguelViewSet(ModelViewSet):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer