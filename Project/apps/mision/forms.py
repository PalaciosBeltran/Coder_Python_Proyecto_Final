from django import forms
from .models import Mision

class MisionForm(forms.ModelForm):
    class Meta:
        model = Mision
        fields = "__all__"
