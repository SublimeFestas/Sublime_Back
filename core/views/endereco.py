from rest_framework.viewsets import ModelViewSet

from core.models import Endereco
from core.serializers.endereco import EnderecoSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        elif self.action == 'me':
            return [IsAuthenticated()]
        return [AllowAny()]
