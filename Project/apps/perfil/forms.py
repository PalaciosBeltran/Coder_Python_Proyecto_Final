from django import forms
from .models import Perfil, PerfilCategoria

class PerfilCategoriaForm(forms.ModelForm):
    class Meta:
        model = PerfilCategoria
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = "__all__"