
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm

from service.models import Service


@method_decorator(login_required,name="dispatch")
class ProfileUpdate(UpdateView):
    form_class= ProfileForm

    success_url= reverse_lazy("profile")
    template_name="registration/profile_form.html"


    def get_object(self):
        profile, created = Profile.objects.get_or_create(usuario_id=self.request.user.id)

        # Obtener todos los servicios del usuario
        servicios = Service.objects.filter(usuario_id=self.request.user.id)

        # Verificar si hay al menos dos servicios y asignar el segundo

        profile.negocio = servicios[0]



        return profile



