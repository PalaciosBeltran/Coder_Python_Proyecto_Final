from django.db import models
from django.utils import timezone

class Mision(models.Model):    
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, blank=True, null=True, verbose_name="descripción")
    imagen = models.URLField(null=True)
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualización")

    class Meta:
        verbose_name = "misión"
        verbose_name_plural = "misiones"

    def __str__(self):
        return self.titulo