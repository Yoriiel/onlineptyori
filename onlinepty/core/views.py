from django.shortcuts import render
from service.models import Category,sonline
from django.db.models import Count
from core.models import Tablero
# Create your views here.

def nosotros(request):
        contador = Category.objects.annotate(num_servicios=Count('get_service'))
        son= sonline.objects.all()
        tableros = Tablero.objects.all();
        return render(request,"core/nosotros.html",{'contador':contador,'sonline':son,'tablero':tableros})




