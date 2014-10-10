from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime


class Categoria(models.Model):
	nome = models.CharField(max_length=255)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
		ordering = ['nome']


class Post(models.Model):
	titulo = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)
	publicado = models.BooleanField(default=True)
	categoria = models.ForeignKey(Categoria)
	imagem = models.ImageField(upload_to = 'banners/', max_length=255, null=True)
	conteudo = models.TextField('Conteúdo')

	criado = models.DateTimeField('Criado em', auto_now_add=True)
	modificado = models.DateTimeField('Modificado em', auto_now=True)

	autor = models.ForeignKey(User)

	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo+ "-" +str(datetime.now()))
		super(Post, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		ordering = ['-id']