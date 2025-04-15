from django.db import models

class Aluguel(models.Model):
    data_festa = models.DateTimeField(verbose_name='Data da festa')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    salao = models.ForeignKey('core.Salao', on_delete=models.CASCADE, verbose_name='Salão')
    desc_festa = models.TextField(verbose_name='Descrição da festa')

    def __str__(self):
        return f'Aluguel no salão {self.salao.id} em {self.data_festa}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['salao', 'data_festa'], name='unico_aluguel_por_salao_e_data')
        ]
        verbose_name_plural = 'Alugueis'
