from django.contrib import admin
from .models import CategoriaProd, Producto, Accesorio

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):

    readonly_fields =("created","updated")

class ProductoAdmin(admin.ModelAdmin):

    readonly_fields =("created","updated")

class AccesorioAdmin(admin.ModelAdmin):

    readonly_fields =("created","updated")

admin.site.register(CategoriaProd, CategoriaProdAdmin)

admin.site.register(Producto, ProductoAdmin)

admin.site.register(Accesorio, AccesorioAdmin)
