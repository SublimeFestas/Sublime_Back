from turtle import mode
from django.db import models

class Salao(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name='Nome do salão')
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE, verbose_name='Endereco')

    class Meta:
        verbose_name_plural = 'Saloes'

    def __str__(self):
        return f'{self.nome} ({self.endereco.bairro}, {self.endereco.cidade})'	

class TelefoneSalao(models.Model):
    salao = models.ForeignKey(Salao, on_delete=models.CASCADE, related_name='telefones', verbose_name='Salao')
    numero = models.CharField(max_length=15, verbose_name='Número do telefone')
    
    def __str__(self):
        return f'{self.salao.nome} ({self.numero})'