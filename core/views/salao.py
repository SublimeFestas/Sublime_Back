from rest_framework.viewsets import ModelViewSet

from core.models import Salao
from core.serializers.salao import SalaoSerializer

class SalaoViewSet(ModelViewSet):
    queryset = Salao.objects.all()
    serializer_class = SalaoSerializer
    
