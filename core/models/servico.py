from django.db import models
from uploader.models import Image

class ServicoAdicional (models.Model):
    nomeServico = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    foto_servico = models.ForeignKey(Image, related_name='servico_foto', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.nomeServico}: {self.valor}'

    class Meta:
        verbose_name_plural = 'Serviços Adicionais'