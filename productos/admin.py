from django.contrib import admin
from productos.models import Productos, Marcas, Tipo, Distribuidores, Distribuidores_Marcas

# Register your models here.
admin.site.register(Productos)
admin.site.register(Marcas)
admin.site.register(Tipo)
admin.site.register(Distribuidores)
admin.site.register(Distribuidores_Marcas)

class Display(admin.ModelAdmin):
    list_display = ("nombre", "marca", "modelo", "sku")


