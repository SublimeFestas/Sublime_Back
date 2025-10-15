from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Aluguel

@receiver(post_save, sender=Aluguel)
def enviar_email_confirmacao(sender, instance, created, **kwargs):
    if created:  
        assunto = "Confirmação da sua locação"
        mensagem = (
            f"Olá {instance.cliente_nome},\n\n"
            f"Sua locação do salão foi confirmada para o dia {instance.data_evento}.\n"
            f"Valor total: R$ {instance.valor_total}\n\n"
            "Agradecemos pela preferência!\nEquipe do Salão"
        )
        remetente = None  
        destinatarios = [instance.cliente_email]

        send_mail(assunto, mensagem, remetente, destinatarios)