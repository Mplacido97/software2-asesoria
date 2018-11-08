from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from alumno.forms import *
from alumno.models import *
from profesor.models import *
import datetime

#               Utils

inicio_clases = datetime.datetime(2018, 8, 6)

#######################################


ALUMNO = 'ALUMNO'

# Create your views here.
def home(request):
    delta_date = datetime.datetime.now() - inicio_clases
    num_semana = round(delta_date.days / 7)
    user_id = request.session.get('user', None)
    type = request.session.get('type', None)
    if type == ALUMNO:
        user = Alumno.objects.filter(pk=user_id).first()
        if user != None:
            return render(request,'alumno/Tony/home.html', {"usuario": user, "num_semana": num_semana})
    return redirect('/alumno/login')



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            codigoUlima = form.cleaned_data['codigoUlima']
            password = form.cleaned_data['password']
            boo, alumno = Alumno.verify_user(codigoUlima, password)
            if boo:
                request.session['user'] = alumno.pk
                request.session['type'] = ALUMNO
                return redirect('/alumno/home')

    form = LoginForm()
    args = {'form': form}
    return render(request,'alumno/login.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/alumno/login')
        print(form.errors)

    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'alumno/reg_form.html', args)


def lista_profesores(request):
    user_id = request.session.get('user', None)
    user = Alumno.objects.filter(pk=user_id).first()
    if user != None:
        profesores = Profesor.objects.all()
        args = {"profesores": profesores, "usuario": user}
        return render(request, 'alumno/Tony/lista_profesores.html', args)
    return redirect('/alumno/login')

def perfil_profesor(request, pk_profesor):
    profesor = Profesor.objects.get(pk= pk_profesor)
    comentarios = []
    total_rate = 0
    num_rate = 0
    for asesoria in profesor.asesoria_set.all():
        for cita in asesoria.cita_set.all():
            for comentario in cita.comentario_set.all():
                comentarios.append(comentario)
                total_rate += comentario.rate
                num_rate +=1


    rate = total_rate / num_rate if num_rate > 0 else " ** No hay Puntuación **"
    args = {"profesor": profesor, "comentarios": comentarios, "rate": rate}
    return render(request, 'alumno/Tony/perfil_profesor.html', args)

def calendar(request, num_semana):
    num_semana = int(num_semana)
    user_id = request.session.get('user', None)
    user = Alumno.objects.filter(pk=user_id).first()
    if user != None:
        citas  = user.cita_set.all()
        favoritos = user.favorito_set.all()
        semana = {
            'Horario': ['7-8', "8-9", '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22'],
            'Lunes': ['']*15,
            'Martes': ['']*15,
            'Miércoles': ['']*15,
            'Jueves': ['']*15,
            'Viernes': ['']*15,
        }
        for favorito in favoritos:
            asesoria = favorito.asesoria
            semana[asesoria.fechaAsesoria][int(asesoria.horaInicio.hour) - 7] = "Favorito: " + asesoria.codCurso.nombreCurso + " - " + asesoria.codCurso.codProfesor.nombrepProfesor + " - " + asesoria.lugar.lugar
        for cita in citas:
            if cita.semana == num_semana:
                asesoria = cita.asesoria
                semana[asesoria.fechaAsesoria][int(asesoria.horaInicio.hour) - 7] = "Cita: " + asesoria.codCurso.nombreCurso + " - " + asesoria.codCurso.codProfesor.nombrepProfesor + " - " + asesoria.lugar.lugar

        profesores = Profesor.objects.all()
        args = {"semana": semana, "usuario": user, "num_semana": num_semana}

        if num_semana > 1:
            args["anterior"] = num_semana - 1
        if num_semana < 16:
            args["siguiente"] = num_semana + 1

        return render(request, 'alumno/Tony/calendar.html', args)
    return redirect('/alumno/login')

def favoritos(request):
    user_id = request.session.get('user', None)
    user = Alumno.objects.filter(pk=user_id).first()
    if user != None:
        favoritos = user.favorito_set.all()
        args = {"favoritos": favoritos, "usuario": user}
        return render(request, 'alumno/Tony/favoritos.html', args)
    return redirect('/alumno/login')

def historial(request):
    user_id = request.session.get('user', None)
    user = Alumno.objects.filter(pk=user_id).first()
    if user != None:
        citas = user.cita_set.all()
        args = {"citas": citas, "usuario": user}
        return render(request, 'alumno/Tony/historial.html', args)
    return redirect('/alumno/login')

def agregar_cita(request, asesoria):
    try:
        user_id = request.session.get('user', None)
        user = Alumno.objects.filter(pk=user_id).first()
        if user != None:
            delta_date = datetime.datetime.now() - inicio_clases
            num_semana = round(delta_date.days / 7)
            asesoria = Asesoria.objects.get(pk = asesoria)
            cita = Cita.objects.create(asesoria=asesoria, alumno=user, semana=num_semana, tema="")
    except Exception as e:
        print(e)
    # print(codCita)
    # print(Cita.objects.get(pk=codCita))
    # return render(request, 'Tony/lista_profesores.html', args)
    profesores = Profesor.objects.all()
    args = {"profesores": profesores, "usuario": request.user}
    return redirect('/alumno/lista_profesores')

def agregar_favorito(request, asesoria):
    try:
        user_id = request.session.get('user', None)
        user = Alumno.objects.filter(pk=user_id).first()
        if user != None:
            asesoria = Asesoria.objects.get(pk = asesoria)
            favorito = Favorito.objects.create(asesoria=asesoria, alumno=user)
    except Exception as e:
        pass
    # print(codCita)
    # print(Cita.objects.get(pk=codCita))
    # return render(request, 'Tony/lista_profesores.html', args)
    profesores = Profesor.objects.all()
    args = {"profesores": profesores, "usuario": request.user}
    return redirect('/alumno/lista_profesores')


def eliminar_favorito(request, favorito):
    Favorito.objects.get(pk=favorito).delete()
    return redirect('/alumno/favoritos')

def eliminar_cita(request, cita):
    Cita.objects.get(pk=cita).delete()
    return redirect('/alumno/historial')

@csrf_exempt
def finalizar_cita(request, cita):
    user_id = request.session.get('user', None)
    user = Alumno.objects.filter(pk=user_id).first()
    if user != None:
        print(user)
        if request.method == 'POST':
            cita = Cita.objects.get(pk = cita)
            Comentario.objects.create(cita= cita, rate = request.POST['rate'], comment= request.POST['comment'])
            cita.finalizado = True
            cita.save()
            return redirect('/alumno/home')
        elif request.method == 'GET':
            return render(request, 'alumno/Tony/finalizar_cita.html', {"cita": cita, "usuario": user})
    else:
        return redirect('/alumno/login')


def log_out(request):
    try:
        del request.session['user']
        del request.session['type']
    except Exception as e:
        pass
    return redirect('/alumno/login')
