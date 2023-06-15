from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("perfil/", include(("perfil.urls", "perfil"))),
    path("mision/", include(("mision.urls", "mision"))),
]
