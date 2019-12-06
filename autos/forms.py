from django import forms
from .models import autos


class autosForm(forms.ModelForm):

    class Meta:
        model = autos
        fields = ['title', 'text', 'author', 'type', 'date_published']
        widgets = {
            'user': forms.HiddenInput(),
        }
