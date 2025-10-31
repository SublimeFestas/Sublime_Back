from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import UserCreateSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import UserFilter


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
