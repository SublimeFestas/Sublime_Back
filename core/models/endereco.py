from django.db import models

class Endereco(models.Model):
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=255, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=255, verbose_name='Bairro')
    cidade = models.CharField(max_length=255, verbose_name='Cidade')
    estado = models.CharField(max_length=2, verbose_name='Estado')
    cep = models.CharField(max_length=10, verbose_name='CEP')

    def __str__(self):
        return f'{self.bairro}, {self.cidade} - {self.estado}'