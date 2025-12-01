from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from core.models import User, Aluguel, ServicoAdicional

class AllValuesViewSet(ModelViewSet):
    http_method_names = ['get']
    def get_queryset(self):
        return User.objects.none()

    def list(self, request, *args, **kwargs):
        data = {
            "total_users": User.objects.count(),
            "total_alugueis": Aluguel.objects.count(),
            "total_servicos": ServicoAdicional.objects.count(),
            "total_alugueis_pagos": Aluguel.objects.filter(status='PAGO').count(),
            "total_alugueis_pendentes": Aluguel.objects.filter(status='PENDENTE').count(),
        }
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)