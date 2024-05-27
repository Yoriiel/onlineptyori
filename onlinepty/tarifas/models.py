from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField
# Create your models here.
# Categorias 
class Tarifas(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nombre")
    content =RichTextField(verbose_name="Contenido",null=True,blank=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    