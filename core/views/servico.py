from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import ServicoAdicional
from core.serializers import ServicoSerializer

class ServicoViewset(ModelViewSet):
    queryset = ServicoAdicional.objects.all()
    serializer_class = ServicoSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        elif self.action == 'me':
            return [IsAuthenticated()]
        return [AllowAny()]
