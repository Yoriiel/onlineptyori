from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import formulario_contacto
from service.models import Category,Slider
from django.db.models import Count
from django.core.mail import EmailMessage
from core.models import Tablero
# Create your views here.
def contacto(request):
        contact_forms=formulario_contacto()
        slide = Slider.objects.all()
        tableros = Tablero.objects.all();
        contador = Category.objects.annotate(num_servicios=Count('get_service'))
        if request.method == 'POST':
                contact_forms = formulario_contacto(data=request.POST)
                if contact_forms.is_valid():
                        name= request.POST.get('name','')
                        email= request.POST.get('email','')
                        content= request.POST.get('content','')

                        #enviamos correo y redireccionamos

                        enviar = EmailMessage(
                                "ONLINEPTY: Nuevo mensaje ",
                                " {}\n\nEscribio:\n\n{},".format(name,content),
                                "{}".format(email),
                                ["javier.solis@utp.ac.pa"],
                                reply_to=[email]
                        )
                        try:
                                enviar.send()
                                return redirect(reverse('contacto')+"?ok")
                        except:
                                return redirect(reverse('contacto')+"?Fail")
        return render(request,"contacto/contacto.html",{'formulario':contact_forms,'slider':slide,'contador':contador,'tablero':tableros})