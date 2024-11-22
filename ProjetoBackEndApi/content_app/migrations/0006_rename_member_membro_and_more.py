# Generated by Django 5.1.3 on 2024-11-21 22:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0005_rename_destinatario_convite_userdestinatario_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Membro',
        ),
        migrations.RenameField(
            model_name='convite',
            old_name='userDestinatario',
            new_name='destinatario',
        ),
        migrations.RenameField(
            model_name='convite',
            old_name='userRemetente',
            new_name='remetente',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='member',
            new_name='membro',
        ),
        migrations.RenameField(
            model_name='membro',
            old_name='user',
            new_name='usuario',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='tipo',
            field=models.CharField(choices=[('Comentários gerais', 'Comentários gerais'), ('Sugestões de melhoria', 'Sugestões de melhoria'), ('Problemas técnicos', 'Problemas técnicos')], default='Comentários gerais', max_length=50),
        ),
    ]