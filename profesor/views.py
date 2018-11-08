from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from profesor.forms import *
from profesor.models import *
from alumno.models import Cita
# Create your views here.

PROFESOR = 'PROFESOR'


def home(request):
    user_id = request.session.get('user', None)
    type = request.session.get('type', None)
    if type == PROFESOR:
        user = Profesor.objects.filter(pk=user_id).first()
        if user != None:
            return render(request,'profesor/Tony/home.html', {"usuario": user})
    return redirect('/profesor/login')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            codigoUlima = form.cleaned_data['codigoUlima']
            password = form.cleaned_data['password']
            boo, profesor = Profesor.verify_user(codigoUlima, password)
            if boo:
                request.session['user'] = profesor.pk
                request.session['type'] = PROFESOR
                return redirect('/profesor/home')

    form = LoginForm()
    args = {'form': form}
    return render(request,'profesor/login.html', args)

def historial(request):
    user_id = request.session.get('user', None)
    user = Profesor.objects.filter(pk=user_id).first()
    if user != None:
        args = {"citas": citas, "usuario": user}
        return render(request, 'profesor/Tony/historial.html', args)
    return redirect('/profesor/login')

def citas(request):
    user_id = request.session.get('user', None)
    user = Profesor.objects.filter(pk=user_id).first()
    if user != None:
        asesorias = user.asesoria_set.all()
        args = {"asesorias": asesorias, "usuario": user}
        return render(request, 'profesor/Tony/citas.html', args)
    return redirect('/profesor/login')

def eliminar_cita(request, cita):
    Cita.objects.get(pk=cita).delete()
    return redirect('/profesor/citas')

@csrf_exempt
def change_state(request):
    state = request.POST['state']
    user_id = request.session.get('user', None)
    user = Profesor.objects.filter(pk=user_id).first()
    if user != None:
        user.state = state
        user.save()
    return ''

def calendar(request):
    user_id = request.session.get('user', None)
    user = Profesor.objects.filter(pk=user_id).first()
    if user != None:
        asesorias  = user.asesoria_set.all()
        semana = {
            'Horario': ['7-8', "8-9", '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22'],
            'Lunes': ['']*15,
            'Martes': ['']*15,
            'Miércoles': ['']*15,
            'Jueves': ['']*15,
            'Viernes': ['']*15,
        }
        for asesoria in asesorias:
            semana[asesoria.fechaAsesoria][int(asesoria.horaInicio.hour) - 7] = "Favorito: " + asesoria.codCurso.nombreCurso + " - " + user.nombrepProfesor + " - " + asesoria.lugar.lugar

        args = {"semana": semana, "usuario": user}
        return render(request, 'profesor/Tony/calendar.html', args)
    return redirect('/profesor/login')


def perfil_profesor(request):
    comentarios = []
    total_rate = 0
    num_rate = 0

    user_id = request.session.get('user', None)
    user = Profesor.objects.filter(pk=user_id).first()
    if user != None:
        for asesoria in user.asesoria_set.all():
            for cita in asesoria.cita_set.all():
                for comentario in cita.comentario_set.all():
                    comentarios.append(comentario)
                    total_rate += comentario.rate
                    num_rate +=1
        rate = total_rate / num_rate if num_rate > 0 else " ** No hay Puntuación **"
        args = {"profesor": user, "comentarios": comentarios, "rate": rate}
        return render(request, 'profesor/Tony/perfil_profesor.html', args)
    return redirect('/profesor/login')


def log_out(request):
    try:
        del request.session['user']
        del request.session['type']
    except Exception as e:
        pass
    return redirect('/profesor/login')
