from django.contrib import admin
from datetime import datetime
from .models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	list_display_links = ('id', 'nome')



class PostAdmin(admin.ModelAdmin):
	fields = ('titulo', 'publicado', 'categoria', 'imagem', 'conteudo')
	list_display = ('id','imagem', 'titulo', 'publicado', 'autor')
	list_display_links = ('id', 'titulo')
	list_filter = ('criado', 'publicado', 'autor')
	search_fields = ('titulo', 'conteudo')

	def get_queryset(self, request):
		qs = super(PostAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(autor=request.user)

	def save_model(self, request, obj, form, change):
		if not obj.id:
			obj.criado = datetime.now()

		if not change:
			obj.autor = request.user
		obj.save()


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)