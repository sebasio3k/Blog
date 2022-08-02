from django.db import models

from ckeditor.fields import RichTextField



# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Categoría Activa/No Activa', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre(s) de Autor', max_length=255, null=False, blank=False)
    apellidos = models.CharField('Apellidos de Autor', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Website', null=True, blank=True)
    correo = models.EmailField('Correo Electrónico', null=False, blank=False)
    estado = models.BooleanField('Autor Activo/No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f'{self.apellidos}, {self.nombre}'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=90, null=False, blank=False)
    slug = models.CharField('slug', max_length=100, null=False, blank=False)
    descripcion = models.CharField('Descripción', max_length=110, null=False, blank=False)
    contenido = RichTextField('Contenido')
    imagen = models.URLField('imagen', max_length=255, null=True, blank=True)
    estado = models.BooleanField('Publicada/No Publicada', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
