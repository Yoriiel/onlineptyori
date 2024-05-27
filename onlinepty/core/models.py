from django.db import models

#slider_onlinepty
class Tablero(models.Model):
    name=models.CharField(verbose_name="nombre",max_length=200,null=True,blank=True)
    texto=models.CharField(verbose_name="texto",max_length=200,null=True,blank=True)


    class Meta:
        verbose_name = "Tablero"
        verbose_name_plural = "Tablero_de_online"

    def __str__(self):
        return self.name
