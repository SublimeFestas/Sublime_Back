import django_filters
from django.db.models import Q
from core.models import Aluguel, User, ServicoAdicional

class AluguelFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search', label='Buscar')

    class Meta:
        model = Aluguel
        fields = []

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(user__name__icontains=value) |
            Q(user__email__icontains=value) |
            Q(data__icontains=value) |
            Q(user__telefones__numero__icontains=value) |
            Q(valor_festa__icontains=value)
    )


class UserFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search', label='Buscar')

    class Meta:
        model = User
        fields = []

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(email__icontains=value) |
            Q(telefones__numero__icontains=value)
        )

class ServicoFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search', label='Buscar')

    class Meta:
        model = ServicoAdicional
        fields = []

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(nomeServico__icontains=value) |
            Q(descricao__icontains=value) |
            Q(valor__icontains=value)
        )