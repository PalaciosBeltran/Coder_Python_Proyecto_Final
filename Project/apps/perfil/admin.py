from django.contrib import admin

from . import models

admin.site.site_title = "Perfil"
admin.site.site_header = "Iniciativa Vengadores"


@admin.register(models.PerfilCategoria)
class PerfilCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)


@admin.register(models.Perfil)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "categoria",
        "nombre",
        "alias",
        "origen",
        "realidad",
        "lugar_nacimiento",
        "descripcion",
        "imagen",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = (
        "categoria",
        "nombre",
    )
    list_filter = ("categoria",)
    date_hierarchy = "fecha_actualizacion"
