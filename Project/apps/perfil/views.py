from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

class PerfilCategoriaListView(ListView):
    model = models.PerfilCategoria
    perfilcategoria_list = models.PerfilCategoria.objects.all()

class PerfilListView(ListView):
    model = models.Perfil

    def get_queryset(self):
        perfil_list = models.Perfil.objects.filter(categoria__nombre="Superhéroe")
        return perfil_list

class PerfilVillanoListView(ListView):
    model = models.Perfil

    def get_queryset(self):
        perfil_list = models.Perfil.objects.filter(categoria__nombre="Villano")
        return perfil_list

class PerfilDetalle(DetailView):
    model = models.Perfil    

class PerfilRegistrar(CreateView):
    categoria = "Superhéroe"
    model = models.Perfil
    form_class = forms.PerfilForm
    success_url = reverse_lazy("perfil:perfil_list")

class PerfilReportar(CreateView):
    categoria = "Villano"
    model = models.Perfil
    form_class = forms.PerfilForm
    success_url = reverse_lazy("perfil:perfilvillano_list")

class PerfilEliminar(DeleteView):
    model = models.Perfil
    success_url = reverse_lazy("perfil:perfil_list")

class PerfilActualizar(UpdateView):
    model = models.Perfil
    success_url = reverse_lazy("perfil:perfil_list")
    form_class = forms.PerfilForm
