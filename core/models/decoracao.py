from django.db import models

class Decoracao(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name='Nome da decoração')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço da decoração')
    descricao = models.TextField(verbose_name='Descrição da decoração') 

    def __str__(self):
        return f'{self.nome} - R$ {self.preco}'

    class Meta:
        verbose_name_plural = 'Decorações'