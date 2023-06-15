from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.MisionListView.as_view(), name="mision_list"),
    path("detalle/<int:pk>", views.MisionDetalle.as_view(), name="mision_detalle"),
    path("registrar", staff_member_required(views.MisionRegistrar.as_view(template_name="mision/mision_registrar.html")), name="mision_registrar"),
    path("detalle/<int:pk>/eliminar", staff_member_required(views.MisionEliminar.as_view(template_name="mision/mision_eliminar.html")), name="mision_eliminar"),
    path("detalle/<int:pk>/actualizar", staff_member_required(views.MisionActualizar.as_view(template_name="mision/mision_registrar.html")), name="mision_actualizar"),
]
urlpatterns += staticfiles_urlpatterns()