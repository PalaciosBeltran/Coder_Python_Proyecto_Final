# Generated by Django 4.2.1 on 2023-06-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_perfil_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilcategoria',
            name='imagen',
            field=models.URLField(null=True),
        ),
    ]
