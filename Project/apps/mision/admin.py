from django.contrib import admin

from . import models

admin.site.site_title = "Mision"
admin.site.site_header = "Iniciativa Vengadores"


@admin.register(models.Mision)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "descripcion",
        "imagen",
    )
    list_display_links = ("titulo",)
    search_fields = ("titulo",)
    ordering = (
        "titulo",
    )
    list_filter = ("titulo",)
    date_hierarchy = "fecha_actualizacion"