# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome'],
                'verbose_name': 'Categoria',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('publicado', models.BooleanField(default=True)),
                ('imagem', models.ImageField(upload_to='images/banners/', max_length=255, null=True, blank=True)),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(to='blog.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ['-id'],
                'verbose_name': 'Post',
            },
            bases=(models.Model,),
        ),
    ]
