# Generated by Django 5.0.4 on 2024-06-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Nombre clave')),
                ('name', models.CharField(max_length=200, verbose_name='Red social')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Enlaces',
                'verbose_name_plural': 'enlacescategoria',
                'ordering': ['name'],
            },
        ),
    ]
