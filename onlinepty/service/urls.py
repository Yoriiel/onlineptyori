from django.urls import path
from . import views
from .views import PageCreate,PageUpdate

urlpatterns = [
    path('',views.home, name="home"),
    path('service/despliegue/<int:category_id>/',views.despliegue, name="despliegue"),
    path('service/resultado/',views.resultado, name="resultado"),
     path('create/',PageCreate.as_view(), name='create'),
    path('update/<int:pk>/',PageUpdate.as_view(), name='update'),
    path('service/producto/<int:title_id>/',views.producto, name="producto"),




]