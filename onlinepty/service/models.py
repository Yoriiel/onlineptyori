from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
# Categorias
class Category(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nombre")
    path =models.CharField(max_length=10000, verbose_name="Path1",null=True,blank=True)
    path1 =models.CharField(max_length=10000, verbose_name="Path2",null=True,blank=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name



#ubicacion

class provincia(models.Model):
    name_provincia=models.CharField(max_length=100, verbose_name="Nombre",null=True,blank=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ['-created']

    def __str__(self):
        return self.name_provincia

# Negocios
class Service(models.Model):
    usuario_id = models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name="get_us")
    title = models.CharField(max_length=200, verbose_name="titulo")
    subtitle =models.CharField(max_length=200, verbose_name="subtitulo")
    content =RichTextField(verbose_name="Contenido")
    published= models.DateTimeField(verbose_name="Fecha de publicacion",default=now)
    image = models.ImageField(verbose_name="imagen", upload_to="services",null=True,blank=True)
    image1 = models.ImageField(verbose_name="imagen1", upload_to="services",null=True,blank=True)
    image2 = models.ImageField(verbose_name="imagen2", upload_to="services",null=True,blank=True)
    video = models.URLField(verbose_name="Video", null=True, blank=True)
    categoria=models.ManyToManyField(Category, verbose_name="categorias",related_name="get_service")
    telefono_regex = RegexValidator( regex=r'^[6-9]\d{7}$', message="El número de teléfono debe estar en un formato válido.")
    telefono = models.CharField(max_length=20, validators=[telefono_regex],null=True,blank=True)
    instagram= models.URLField(null=True,blank=True,)
    gps= models.URLField(null=True,blank=True,max_length=1000)
    ubicacion = models.ManyToManyField(provincia,verbose_name="Provincias")
    rating=models.IntegerField(range(1,5),null=True,blank=True)
    distrito=models.CharField(max_length=200, verbose_name="Distrito",null=True,blank=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title


#enlace redes de la empresa
class Links(models.Model):
    key= models.SlugField(verbose_name="nombre Clave", max_length=200, unique=True)
    name=models.CharField(verbose_name="nombre",max_length=200,null=True,blank=True)
    url=models.URLField(verbose_name="Enlace",max_length=200,null=True,blank=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ['-created']

    def __str__(self):
        return self.name


#Slider
class Slider(models.Model):
    name=models.CharField(verbose_name="nombre",max_length=200,null=True,blank=True)
    image = models.ImageField(verbose_name="imagen", upload_to="services",null=True,blank=True)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return self.name


#slider_onlinepty
class sonline(models.Model):
    name=models.CharField(verbose_name="nombre",max_length=200,null=True,blank=True)
    image = models.ImageField(verbose_name="imagen", upload_to="services",null=True,blank=True)

    class Meta:
        verbose_name = "Slider_de_online"
        verbose_name_plural = "Sliders_de_online"

    def __str__(self):
        return self.name





