from rest_framework.viewsets import ModelViewSet
from core.models import Aluguel
from core.serializers.aluguel import AluguelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import AluguelFilter
from rest_framework.permissions import IsAuthenticated

class AluguelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AluguelFilter

class AlugueisPorUsuarioViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer

    def get(self, request, user_id):
        alugueis = Aluguel.objects.filter(user__id=user_id)
        serializer = AluguelSerializer(alugueis, many=True)
        return Response(serializer.data)