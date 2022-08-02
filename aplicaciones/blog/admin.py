from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Barra de busqueda:
    search_fields = ['nombre', 'estado']
    # Para atributos en vista de registros:
    list_display = ['id', 'nombre', 'estado', 'fecha_creacion']
    resource_class = CategoriaResource


class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Barra de busqueda:
    search_fields = ['nombre', 'apellidos', 'estado']
    # Para atributos en vista de registros:
    list_display = [
        'id',
        'nombre',
        'apellidos',
        'correo',
        'fecha_creacion',
        'estado',
        'facebook',
        'twitter',
        'instagram',
        'web',
    ]
    resource_class = AutorResource


class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'titulo', 'slug', 'estado', 'descripcion']
    list_display = [
        'id',
        'titulo',
        'slug',
        'descripcion',
        'contenido',
        'imagen',
        'estado',
        'fecha_creacion',
        'autor',
        'categoria',
    ]
    resource_class = PostResource


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
