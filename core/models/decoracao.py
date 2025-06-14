from asyncio.windows_events import NULL
from django.db import models
from uploader.models import Image

class Decoracao(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name='Nome da decoração')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço da decoração')
    descricao = models.TextField(verbose_name='Descrição da decoração')

    def __str__(self):
        return f'{self.nome} - R$ {self.preco}'

    class Meta:
        verbose_name_plural = 'Decorações'

class FotoDecoracao(models.Model):
    decoracao = models.ForeignKey(Decoracao, on_delete=models.CASCADE, related_name='fotos_decoracao', verbose_name='Decoração')
    imagem = models.ForeignKey(Image, related_name="+", on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Imagem', default=NULL)

    def __str__(self):
        return f'Foto da decoração {self.decoracao.nome}'

    class Meta:
        verbose_name_plural = 'Fotos de Decorações'