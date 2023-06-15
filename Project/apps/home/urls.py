from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("about/", views.about, name="about"),
]
urlpatterns += staticfiles_urlpatterns()