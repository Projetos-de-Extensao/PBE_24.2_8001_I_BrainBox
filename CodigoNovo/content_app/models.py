from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Member(models.Model):
    nome = models.CharField(max_length=255)
    convites_enviados = models.ManyToManyField('Convite', related_name='convites_enviados', blank=True)
    convidados = models.ManyToManyField('self', blank=True, symmetrical=False)
    convidante = models.ForeignKey(User, related_name='members', on_delete=models.CASCADE)

    def gerar_link_convite(self):
        # Lógica para gerar um convite para um novo membro
        pass

    def autenticar(self):
        # Lógica para autenticação do membro
        pass

    def __str__(self):
        return self.nome

class Convite(models.Model):
    ESTADOS = [
        ('pendente', 'Pendente'),
        ('usado', 'Usado'),
        ('expirado', 'Expirado'),
    ]

    link = models.CharField(max_length=255)
    data_envio = models.DateTimeField(default=timezone.now)
    data_expiracao = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendente')
    membro_convindante = models.ForeignKey(Member, related_name='convites_feitos', on_delete=models.CASCADE)
    membro_convidado = models.ForeignKey(Member, related_name='convites_recebidos', null=True, blank=True, on_delete=models.SET_NULL)

    def verificar_validade(self):
        return timezone.now() < self.data_expiracao

    def vincular_convidado(self, membro):
        self.membro_convidado = membro
        self.estado = 'usado'
        self.save()

    def __str__(self):
        return f"Convite {self.id} - {self.estado}"

class Cadastro(models.Model):
    membro = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    convite_usado = models.ForeignKey(Convite, on_delete=models.CASCADE)

    def validar_convite(self):
        return self.convite_usado.verificar_validade()

    def registrar_membro(self):
        # Lógica para registrar um novo membro usando o convite
        pass

    def __str__(self):
        return f"Cadastro {self.id} para {self.membro.nome}"

class SistemaConvite(models.Model):
    limite_convites = models.IntegerField()

    def gerar_convite(self, membro):
        # Lógica para gerar um convite
        pass

    def validar_convite(self, convite):
        return convite.verificar_validade()

    def controlar_limite(self):
        # Lógica para controlar o limite de convites
        pass

    def __str__(self):
        return f"Sistema de Convites - Limite: {self.limite_convites}"
