# Generated by Django 5.0.4 on 2024-06-03 18:30

import datetime
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
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='contenido')),
                ('published', models.DateTimeField(default=datetime.datetime(2024, 6, 3, 18, 30, 31, 996161, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicacion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='imagen')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de edicion')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('categories', models.ManyToManyField(to='blog.categoria', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'titulo',
                'verbose_name_plural': 'titulos',
                'ordering': ['-created'],
            },
        ),
    ]
