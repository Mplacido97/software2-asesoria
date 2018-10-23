from django import forms
from profesor.models import *
# from django.contrib.auth.models import User

class LoginForm(forms.Form):
    codigoUlima = forms.CharField(label='Código ULima', required=True)
    password = forms.CharField(label='Contraseña', required=True)

    class Meta:
        model = Profesor
        fields = {
            'codigoUlima',
            'password'
        }
