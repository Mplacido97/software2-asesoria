from django import forms
from alumno.models import *
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        }

class LoginForm(forms.Form):
    codigoUlima = forms.CharField(label='Código ULima', required=True)
    password = forms.CharField(label='Contraseña', required=True)

    class Meta:
        model = Alumno
        fields = {
            'codigoUlima',
            'password'
        }
