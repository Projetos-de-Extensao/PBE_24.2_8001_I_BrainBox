from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
import pytz


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    convites_aceitos = models.IntegerField(default=0)

    def enviar_convite(self, email_destinatario):
        if self.n_convites >= 5:
            raise ValueError("Limite de convites mensais atingido.")
        convite = Convite.objects.create(userRemetente=self, userDestinatario=email_destinatario)
        self.convites_enviados.add(convite)
        self.save()
        return convite

    def contar_convites_mes_atual(self):
        agora = timezone.now()
        inicio_mes = agora.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        return self.convites_enviados.filter(data_envio__gte=inicio_mes).count()
    
    @property
    def n_convites(self):
        return self.contar_convites_mes_atual()

    def verificar_convites_aceitos(self):
        convites_aceitos = self.convites_enviados.filter(status='Aceito').count()
        self.convites_aceitos = convites_aceitos
        Member.objects.filter(pk=self.pk).update(convites_aceitos=convites_aceitos)

    def enviar_feedback(self, feedback_texto, tipo):
        feedback = Feedback.objects.create(member=self, feedback=feedback_texto, tipo=tipo)
        return feedback
    
    def listar_feedbacks(self):
        return Feedback.objects.filter(member=self)

    def __str__(self):
        return self.user.username
    

class Convite(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Aceito', 'Aceito'),
        ('Expirado', 'Expirado'),
    ]
    userRemetente = models.ForeignKey(Member, related_name='convites_enviados', on_delete=models.CASCADE)
    userDestinatario = models.EmailField(unique=True)
    link = models.CharField(blank=True, max_length=255, unique=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pendente')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Convite para {self.userDestinatario} - Status: {self.status} - Token: {self.link}"

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = str(uuid.uuid4())
        self.data_envio = timezone.now().astimezone(pytz.timezone('America/Sao_Paulo'))
        self.is_expirado()
        super().save(*args, **kwargs)
        self.userRemetente.verificar_convites_aceitos()

    def is_expirado(self):
        validade = self.data_envio + timedelta(days=7)
        if timezone.now() > validade:
            self.status = 'Expirado'
            self.save()
            return True
        return False


class Feedback(models.Model):
    TIPO_CHOICES = [
        ('Comentários gerais', 'Comentários gerais'),
        ('Sugestões de melhoria', 'Sugestões de melhoria'),
        ('Problemas tecnicos', 'Problemas tecnicos'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='feedback')
    feedback = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, default='Comentários gerais')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} : feito por {self.member.user.username} -> {self.data}'


@receiver(post_save, sender=User)
def create_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_member(sender, instance, **kwargs):
    instance.member.save()