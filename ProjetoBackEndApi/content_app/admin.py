from django.contrib import admin
from content_app import models
from .models import Convite, Member,Feedback

# Inline para exibir convites na página de detalhes de um Member
class ConviteInline(admin.TabularInline):
    model = Convite
    fields = ['userDestinatario', 'status', 'link', 'data_envio']
    readonly_fields = ['link', 'data_envio']  # Campos de leitura

from django.core.exceptions import ValidationError

from django.core.exceptions import ValidationError

class ConviteAdmin(admin.ModelAdmin):
    exclude = ('userRemetente', 'link')  # Oculta os campos no Django Admin

    def save_model(self, request, obj, form, change):
        limite_convites = 5
        if obj.userRemetente.convites_enviados.count() >= limite_convites:
            raise ValidationError(f"O número de convites enviados foi atingido. Você não pode enviar mais de {limite_convites} convites.")
        else:
            if not obj.userRemetente_id:
                obj.userRemetente = request.user.member
                obj.save()




class FeedbackInline(admin.TabularInline):
    model = Feedback
    fields = ['feedback', 'data', 'tipo']
    readonly_fields = ['data']  # Campos de leitura
class FeedbackAdmin(admin.ModelAdmin):
    exclude = ('member',)  # Oculta o campo member no FeedbackAdmin

    def save_model(self, request, obj, form, change):
        if hasattr(request.user, 'member'):
            obj.member = request.user.member  # Define o member como o perfil do usuário logado
            obj.save()
        else:
            raise ValueError("O usuário logado não possui um perfil.")

class MemberAdmin(admin.ModelAdmin):
    exclude = ('user',)  # Oculta campos específicos
    inlines = [ConviteInline, FeedbackInline]  # Adiciona convites na página de detalhes de um Member
    list_display = ('user', 'convites_aceitos', 'convites_qtd')  # Exibe 'convites_qtd' na lista de membros

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        obj.save()


# Registra os modelos no Django Admin
admin.site.register(Member, MemberAdmin)
admin.site.register(Convite, ConviteAdmin)
admin.site.register(Feedback, FeedbackAdmin)
