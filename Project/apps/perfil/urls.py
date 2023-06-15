from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.PerfilCategoriaListView.as_view(), name="perfilcategoria_list"),
    path("heroe", views.PerfilListView.as_view(), name="perfil_list"),
    path("villano", views.PerfilVillanoListView.as_view(), name="perfilvillano_list"),
    path("detalle/<int:pk>", views.PerfilDetalle.as_view(), name="perfil_detalle"),
    path("registrar", staff_member_required(views.PerfilRegistrar.as_view(template_name="perfil/perfil_registrar.html")), name="perfil_registrar"),
    path("reportar", staff_member_required(views.PerfilReportar.as_view(template_name="perfil/perfil_reportar.html")), name="perfil_reportar"),
    path("detalle/<int:pk>/eliminar", staff_member_required(views.PerfilEliminar.as_view(template_name="perfil/perfil_eliminar.html")), name="perfil_eliminar"),
    path("detalle/<int:pk>/actualizar", staff_member_required(views.PerfilActualizar.as_view(template_name="perfil/perfil_registrar.html")), name="perfil_actualizar"),
]
urlpatterns += staticfiles_urlpatterns()