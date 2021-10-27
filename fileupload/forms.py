from django import forms
from .models import image
class FileForm(forms.ModelForm):
    class Meta:
        model = image
        fields = ['pic']