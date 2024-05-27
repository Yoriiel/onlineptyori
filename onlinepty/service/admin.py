from django.contrib import admin
from .models import Category,Service,provincia,Links,Slider,sonline

# Register your models here.

#categorias
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')

#negocios
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')
    list_display = ('title', 'created', 'updated')
    search_fields = ('title',)


#provincias
class provinciasAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')


#links
class LinksAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(provincia,provinciasAdmin)
admin.site.register(Links,LinksAdmin)
admin.site.register(Slider)
admin.site.register(sonline)