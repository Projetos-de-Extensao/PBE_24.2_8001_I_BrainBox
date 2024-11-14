# Generated by Django 5.1.3 on 2024-11-14 11:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recompensas', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('Comentários gerais', 'Comentários gerais'), ('Sugestões de melhoria', 'Sugestões de melhoria'), ('Problemas tecnicos', 'Problemas tecnicos')], default='Comentários gerais', max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='content_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userDestinatario', models.EmailField(max_length=254, unique=True)),
                ('link', models.CharField(blank=True, max_length=255, unique=True)),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Aceito', 'Aceito'), ('Expirado', 'Expirado')], default='Pendente', max_length=50)),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('userRemetente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_enviados', to='content_app.member')),
            ],
        ),
    ]