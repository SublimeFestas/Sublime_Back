from django.db import models
from django.conf import settings

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comentario = models.TextField()
    nota = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - ({self.nota})"
