from django.contrib import admin
from .models import Tarifas
# Register your models here.
#negocios
class TarifasAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)

admin.site.register(Tarifas,TarifasAdmin)
