# Generated by Django 5.1.3 on 2024-11-14 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='recompensas',
            new_name='convites_aceitos',
        ),
    ]
