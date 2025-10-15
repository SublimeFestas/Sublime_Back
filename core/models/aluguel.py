from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

from core.views import decoracao

from .servico import ServicoAdicional

class Aluguel(models.Model):
    TIPO_LOCACAO_CHOICES = [
        ('SALÃO', 'Salão'),
        ('DECORAÇÃO', 'Decoração'),
        ('AMBOS', 'Salão e Decoração'),
    ]

    tipo_locacao = models.CharField(
        max_length=10,
        choices=TIPO_LOCACAO_CHOICES,
        verbose_name='Tipo da locação',
        default='SALAO',
    )
    data_festa = models.DateField(verbose_name='Data da festa')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    salao = models.ForeignKey(
        'core.Salao',
        on_delete=models.PROTECT,
        verbose_name='Salão',
        null=True,
        blank=True
    )
    #decoracao = models.ForeignKey(
    #    'core.Decoracao',
    #    on_delete=models.PROTECT,
    #    verbose_name='Decoração',
    #    null=True,
    #    blank=True
    #)
    possui_decoracao = models.BooleanField(default=False)
    decoracao = models.TextField(blank=True)
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
       
    def clean(self):
        if self.tipo_locacao == 'SALAO':
            if not self.salao:
                raise ValidationError('Selecione um salão para este tipo de locação.')
            conflito_salao = Aluguel.objects.filter(
                salao=self.salao,
                data_festa=self.data_festa
            ).exclude(pk=self.pk).exists()
            if conflito_salao:
                raise ValidationError('Este salão já está alugado nesta data.')

        elif self.tipo_locacao == 'DECORACAO':
            if not self.decoracao:
                raise ValidationError('Selecione uma decoração para este tipo de locação.')
            conflito_decoracao = Aluguel.objects.filter(
                decoracao=self.decoracao,
                data_festa=self.data_festa
            ).exclude(pk=self.pk).exists()
            if conflito_decoracao:
                raise ValidationError('Esta decoração já está alugada nesta data.')

        elif self.tipo_locacao == 'AMBOS':
            if not self.salao or not self.decoracao:
                raise ValidationError('Selecione salão e decoração para este tipo de locação.')
            conflito_salao = Aluguel.objects.filter(
                salao=self.salao,
                data_festa=self.data_festa
            ).exclude(pk=self.pk).exists()
            if conflito_salao:
                raise ValidationError('Este salão já está alugado nesta data.')
            conflito_decoracao = Aluguel.objects.filter(
                decoracao=self.decoracao,
                data_festa=self.data_festa
            ).exclude(pk=self.pk).exists()
            if conflito_decoracao:
                raise ValidationError('Esta decoração já está alugada nesta data.')

        else:
            raise ValidationError('Tipo de locação inválido.')

    def __str__(self):
        if self.tipo_locacao == 'AMBOS':
            return f'Salão {self.salao} + Decoração {self.decoracao} em {self.data_festa}'
        elif self.tipo_locacao == 'SALAO':
            return f'Salão {self.salao} em {self.data_festa}'
        elif self.tipo_locacao == 'DECORACAO':
            return f'Decoração {self.decoracao} em {self.data_festa}'
        return f'Aluguel em {self.data_festa}'

    class Meta:
        verbose_name_plural = 'Aluguéis'
