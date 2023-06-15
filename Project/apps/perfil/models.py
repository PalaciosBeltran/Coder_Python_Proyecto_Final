from django.db import models
from django.utils import timezone

class PerfilCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    imagen = models.URLField(null=True)

    class Meta:
        verbose_name = "categoría de perfiles"
        verbose_name_plural = "categorías de perfiles"

    def __str__(self):        
        return self.nombre

class Perfil(models.Model):    
    categoria = models.ForeignKey(PerfilCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="categoría")
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    realidad = models.CharField(max_length=50)
    lugar_nacimiento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250, blank=True, null=True, verbose_name="descripción")
    imagen = models.URLField(null=True)
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualización")

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"

    def __str__(self):
        return self.nombre



