# Generated by Django 3.0.3 on 2020-02-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0003_noticia_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.TextField(blank=True, max_length=128, null=True, verbose_name='Autor'),
        ),
    ]
