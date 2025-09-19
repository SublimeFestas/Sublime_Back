from django.db import models
from django.conf import settings
from . import Salao

class Feedback(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    salao = models.ForeignKey(Salao, on_delete=models.CASCADE)
    comentario = models.TextField()
    nota = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'salao')

    def __str__(self):
        return f"{self.usuario} - {self.salao} ({self.nota})"
