from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import forms

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home.html", {"mensaje": f"¡Bienvenido vengador {usuario}!"})
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username") 
            form.save()
            return render(request, "home.html", {"messages": "¡Vengador registrado!"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")