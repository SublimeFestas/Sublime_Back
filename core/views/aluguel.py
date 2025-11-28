from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Aluguel
from core.serializers.aluguel import AluguelSerializer
from core.filters import AluguelFilter

class AluguelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AluguelFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=False, methods=['get'], url_path='por-usuario/(?P<user_id>[^/.]+)')
    def por_usuario(self, request, user_id=None):
        alugueis = Aluguel.objects.filter(user_id=user_id)
        serializer = AluguelSerializer(alugueis, many=True, context=self.get_serializer_context())
        return Response(serializer.data)
