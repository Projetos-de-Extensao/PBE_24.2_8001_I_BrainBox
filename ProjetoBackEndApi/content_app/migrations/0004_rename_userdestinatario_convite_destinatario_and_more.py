# Generated by Django 5.1.3 on 2024-11-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0003_remove_member_convites_aceitos'),
    ]

    operations = [
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
            new_name='Member',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback',
            new_name='texto',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='user',
            new_name='usuario',
        ),
        migrations.AddField(
            model_name='member',
            name='convitesAceitos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='tipo',
            field=models.CharField(choices=[('Comentários gerais', 'Comentários gerais'), ('Sugestões de melhoria', 'Sugestões de melhoria'), ('Problemas técnicos', 'Problemas técnicos')], default='Comentários gerais', max_length=50),
        ),
    ]