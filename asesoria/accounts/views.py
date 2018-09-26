from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from accounts.models import *
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'Tony/home.html', {"usuario": request.user})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
        print(form.errors)

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'reg_form.html', args)


def lista_profesores(request):
    profesores = Profesor.objects.all()
    args = {"profesores": profesores, "usuario": request.user}
    return render(request, 'Tony/lista_profesores.html', args)


def calendar(request):

    user = User.objects.get(username=request.user)
    citas  = user.cita_set.all()

    semana = {
        'Horario': ['7-8', "8-9", '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22'],
        'Lunes': ['']*15,
        'Martes': ['']*15,
        'Miercoles': ['']*15,
        'Jueves': ['']*15,
        'Viernes': ['']*15,
    }

    for cita in citas:
        asesoria = cita.asesoria
        semana[asesoria.fechaAsesoria][int(asesoria.horaInicio.hour) - 7] = asesoria.codCurso.nombreCurso + " - " + asesoria.codCurso.codProfesor.nombrepProfesor + " - " + asesoria.lugar.lugar


    profesores = Profesor.objects.all()
    args = {"semana": semana, "usuario": request.user}
    return render(request, 'Tony/calendar.html', args)


def favoritos(request):
    user = User.objects.get(username=request.user)
    favoritos = user.favorito_set.all()
    args = {"favoritos": favoritos, "usuario": request.user}
    return render(request, 'Tony/favoritos.html', args)

def historial(request):
    user = User.objects.get(username=request.user)
    citas = user.cita_set.all()
    args = {"citas": citas, "usuario": request.user}
    return render(request, 'Tony/historial.html', args)

def agregar_cita(request, codAsesoria):
    try:
        asesoria = Asesoria.objects.get(codAsesoria = codAsesoria)
        user = User.objects.get(username=request.user)
        cita = Cita.objects.create(asesoria=asesoria, alumno=user, tema="")
    except Exception as e:
        pass
    # print(codCita)
    # print(Cita.objects.get(pk=codCita))
    # return render(request, 'Tony/lista_profesores.html', args)
    profesores = Profesor.objects.all()
    args = {"profesores": profesores, "usuario": request.user}
    return redirect('/account/lista_profesores')

def agregar_favorito(request, codAsesoria):
    try:
        asesoria = Asesoria.objects.get(codAsesoria = codAsesoria)
        user = User.objects.get(username=request.user)
        favorito = Favorito.objects.create(asesoria=asesoria, alumno=user)
    except Exception as e:
        pass
    # print(codCita)
    # print(Cita.objects.get(pk=codCita))
    # return render(request, 'Tony/lista_profesores.html', args)
    profesores = Profesor.objects.all()
    args = {"profesores": profesores, "usuario": request.user}
    return redirect('/account/lista_profesores')


def eliminar_favorito(request, codFavorito):
    Favorito.objects.get(pk=codFavorito).delete()
    return redirect('/account/favoritos')
