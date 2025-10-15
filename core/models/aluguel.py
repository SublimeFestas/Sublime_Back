from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

from .servico import ServicoAdicional

class Aluguel(models.Model):
    STATUS_CHOICES = [
        ('PAGO', 'pago'),
        ('PENDENTE', 'pendente'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        verbose_name='status',
        default='PENDENTE',
    )
    data = models.DateField(verbose_name='Data da festa')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    desc_festa = models.TextField(verbose_name='Descrição da festa')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Usuário',
        null=True,
        blank=True
    )
    valor_festa = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Valor total da festa',
        null=True,
        blank=True
    )
    servico = models.ManyToManyField(ServicoAdicional, related_name="servico", blank=True)
       

    def __str__(self):
        return f'Aluguel em {self.data} por {self.user}, status: {self.status}'

    class Meta:
        verbose_name_plural = 'Aluguéis'
