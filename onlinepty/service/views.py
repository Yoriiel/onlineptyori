from django.shortcuts import render,get_object_or_404
from .models import Service,Category,Slider,sonline
from core.models import Tablero
from django.db.models import Count
from django.db.models import    Q
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from .forms import PageForm

# Create your views here.

def home(request):
    servicios = Service.objects.all()
    categories = Category.objects.all()
    contador = Category.objects.annotate(num_servicios=Count('get_service'))
    slide = Slider.objects.all()
    son= sonline.objects.all()
    tableros = Tablero.objects.all();

    return render(request, "service/home.html", {'services': servicios,'categories': categories,'slider':slide,'contador':contador,'sonline':son,'tablero':tableros})


#Resultados de busqueda
def resultado(request):
    servicios = Service.objects.all()
    categories = Category.objects.all()
    busqueda = request.POST.get("buscar")
    provi = request.POST.get("provi")
    son= sonline.objects.all()
    contador = Category.objects.annotate(num_servicios=Count('get_service'))
    tableros = Tablero.objects.all();

    if busqueda and provi:

        servicios =  Service.objects.filter(
            Q(categoria__name__icontains = busqueda) |
            Q(title__icontains = busqueda) ,
            Q(ubicacion__name_provincia__icontains = provi)|
            Q(distrito__icontains = provi),

            ).distinct()

    elif busqueda:
        servicios =  Service.objects.filter(
            Q(categoria__name__icontains = busqueda)|
            Q(title__icontains = busqueda) ,).distinct()
    elif provi:
        servicios =  Service.objects.filter(
             Q(ubicacion__name_provincia__icontains = provi)|
             Q(distrito__icontains = provi)).distinct()


    else:
        pass

    return render(request, "service/resultado.html", {'services': servicios, 'categories': categories,'busqueda':busqueda,'provi':provi,'contador':contador,'sonline':son,'tablero':tableros})



def despliegue(request, category_id):
        categorias = get_object_or_404(Category,id=category_id)
        categories = Category.objects.all()
        ubicacion =Service.objects.all()
        contador = Category.objects.annotate(num_servicios=Count('get_service'))
        son= sonline.objects.all()
        tableros = Tablero.objects.all();
        return render(request, "service/despliegue.html", {'categorias': categorias,'categories': categories,'ubicacion':ubicacion,'contador':contador,'sonline':son,'tablero':tableros})


def producto(request, title_id):
        categorias = get_object_or_404(Service,id=title_id)
        servicios = Service.objects.filter(title=categorias)
        categories = Category.objects.all()
        contador = Category.objects.annotate(num_servicios=Count('get_service'))
        son= sonline.objects.all()
        tableros = Tablero.objects.all();

        return render(request, "service/producto.html", {'categorias': categorias,'categories': categories,'servicios': servicios,'contador':contador,'sonline':son,'tablero':tableros})


@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Service
    form_class = PageForm
    success_url= reverse_lazy('home')

    def form_valid(self, form):
            form.instance.usuario_id = self.request.user  # Asignar el usuario autenticado
            return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Service
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('update',args=[self.object.id])+ '?ok'

