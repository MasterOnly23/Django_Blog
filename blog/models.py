from distutils.command.upload import upload
from email.policy import default
from operator import mod
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Activa/Inactiva ', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoria' #como se identifica el modelo en el admin
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField('Nombres de Autor', max_length = 255, null = False, blank = False)
    apellidos = models.CharField('Apellidos de Autor', max_length = 255, null = False, blank = False)
    web = models.URLField('Web', null =True, blank = True)
    facebook = models.URLField('Facebook', null =True, blank = True)
    twitter = models.URLField('Twitter', null =True, blank = True)
    instagram = models.URLField('Instagram', null =True, blank = True) 
    email = models.EmailField('Email', null = False, blank = False)
    estado = models.BooleanField('Autor Activo/Inactivo', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


    def __str__(self) -> str:
        return "{0},{1}".format(self.apellidos, self.nombres)



class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 90, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    descripcion = models.CharField('Descripcion', max_length = 100, blank = False, null = False)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='img_post', blank = True, null = True)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/Oculto', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return self.titulo



