from django.db import models

class ServicoAdicional (models.Model):
    nomeResponsavel = models.CharField(max_length=255)
    nomeServico = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    email = models.CharField(unique=True)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.nomeServico}: {self.valor}'