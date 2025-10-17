from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Aluguel

@receiver(post_save, sender=Aluguel)
def enviar_email_confirmacao(sender, instance, created, **kwargs):
    if created:  # só envia quando um novo Aluguel for criado
        user = instance.user
        if user and user.email:  # só envia se o usuário tiver e-mail
            print(f"Disparando e-mail para {user.email}")  # debug
            send_mail(
                subject='Confirmação do seu aluguel',
                message=(
                    f'Olá {user.name or user.email}, tudo bem?\n\n'
                    f'Seu aluguel foi registrado com sucesso!\n'
                    f'Data da festa: {instance.data}\n'
                    f'Status: {instance.status}\n'
                    f'Valor total: R$ {instance.valor_festa or "não informado"}\n\n'
                    'Agradecemos por escolher nosso salão 💖'
                ),
                from_email='seuemail@gmail.com',  # seu e-mail configurado no settings.py
                recipient_list=[user.email],
            )
