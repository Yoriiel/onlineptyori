

from django.db import models
from django.contrib.auth.models import User
from service.models import Service

# Create your models here.

class Profile(models.Model):
    nombre= models.CharField(max_length=100,null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    negocio = models.OneToOneField(Service,on_delete=models.CASCADE, null=True)
    Avatar= models.ImageField(upload_to='profiles', null=True,blank=True)
    bio= models.TextField(null=True,blank=True)
    link= models.URLField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"






