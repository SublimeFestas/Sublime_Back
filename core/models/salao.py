from django.db import models
from uploader.models import Image


class Salao(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name='Nome do salão')
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE, verbose_name='Endereco')

    class Meta:
        verbose_name_plural = 'Saloes'

    def __str__(self):
        return f'{self.nome} ({self.endereco.bairro}, {self.endereco.cidade})'	
    
class SalaoFotos(models.Model):
    salao = models.ForeignKey(Salao, related_name='fotos', on_delete=models.CASCADE)
    imagem = models.ForeignKey(Image, related_name="+", on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Imagem', default=null)


    def __str__(self):
        return f"Foto de {self.salao.nome}"

class TelefoneSalao(models.Model):
    salao = models.ForeignKey(Salao, on_delete=models.CASCADE, related_name='telefones', verbose_name='Salão')
    numero = models.CharField(max_length=15, verbose_name='Número do telefone')

    def __str__(self):
        return f'{self.salao.nome} ({self.numero})'