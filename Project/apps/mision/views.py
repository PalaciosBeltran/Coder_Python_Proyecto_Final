from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

class MisionListView(ListView):
    model = models.Mision

class MisionDetalle(DetailView):
    model = models.Mision

class MisionRegistrar(CreateView):
    model = models.Mision
    form_class = forms.MisionForm
    success_url = reverse_lazy("mision:mision_list")

class MisionEliminar(DeleteView):
    model = models.Mision
    success_url = reverse_lazy("mision:mision_list")

class MisionActualizar(UpdateView):
    model = models.Mision
    success_url = reverse_lazy("mision:mision_list")
    form_class = forms.MisionForm

