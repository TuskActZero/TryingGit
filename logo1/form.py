from django import forms
from .models import Persona
from django.forms import ModelForm


class login(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()

class PersonaForm(ModelForm):

    class Meta:
        model = Persona
        fields = ['nombre', 'edad']
