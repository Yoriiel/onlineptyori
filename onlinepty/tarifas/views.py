from django.shortcuts import render
from service.models import Category,Slider
from .models import Tarifas
from django.db.models import Count
from core.models import Tablero
# Create your views here.
def negocios(request):
        tarifa= Tarifas.objects.all();
        slide = Slider.objects.all()
        tableros = Tablero.objects.all();
        contador = Category.objects.annotate(num_servicios=Count('get_service'))
        return render(request,"tarifas/negocios.html",{'contador':contador, 'tarifas':tarifa,'slider':slide,'tablero':tableros})
