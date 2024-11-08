from django.contrib import admin
from content_app import models

admin.site.register(models.Member)
admin.site.register(models.Convite)
admin.site.register(models.Cadastro)
admin.site.register(models.SistemaConvite)