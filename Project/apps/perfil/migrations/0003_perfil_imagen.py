# Generated by Django 4.2.1 on 2023-06-11 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_remove_perfil_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagen',
            field=models.URLField(null=True),
        ),
    ]