from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Telefone(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='telefones')
    numero = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.numero} ({self.usuario.username})"