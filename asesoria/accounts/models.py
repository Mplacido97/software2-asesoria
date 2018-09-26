from django.db import models
import datetime
from django.contrib.auth.models import User
#from django.contrib.auth.model import User
# Create your models here.

#class UserProfile(models.Model):

#    USERS_TYPE = ('Alumno','Profesor')

    #user = models.OnetoOneField(User)
    #tipo = (models.chartField(max_legnth=10, choices = USERS_TYPE))
    #carrera = models.chartField(default=10)


class Alumno(models.Model):

    codigo = models.IntegerField(primary_key = True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo  = models.EmailField()

    def __unicode__(self):
        return self.title

class Profesor(models.Model):
    codProfesor = models.IntegerField(primary_key = True, unique= True)
    nombrepProfesor = models.CharField(max_length=50)
    correo  = models.EmailField()


    def __str__(self):
        return "Codigo: {}, Nombre: {}, Correo: {}".format(self.codProfesor, self.nombrepProfesor, self.correo)


class Curso(models.Model):
    codigoCurso = models.IntegerField(primary_key = True, unique= True)
    nombreCurso = models.CharField(max_length=50)
    seccion = models.IntegerField()
    codProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)


    def __unicode__(self):
        return self.title

class Salon(models.Model):
    lugar = models.CharField(max_length = 10, unique= True)

    def __str__(self):
        return "Lugar: {}".format(self.lugar)

class Asesoria(models.Model):
    dia_semana = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
    )

    codProfesor = models.ForeignKey( Profesor, on_delete=models.CASCADE)
    codAsesoria = models.IntegerField(primary_key = True, unique= True)
    codCurso= models.ForeignKey(Curso, on_delete=models.CASCADE,)
    fechaAsesoria = models.CharField(max_length=12, choices=dia_semana)
    horaInicio = models.TimeField(default="12:00")
    lugar = models.ForeignKey(Salon, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class Cita(models.Model):
    asesoria = models.ForeignKey(Asesoria, on_delete=models.CASCADE)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    #PUEDE MEJORARSE
    tema = models.CharField(max_length=300)

    class Meta:
        unique_together = ('asesoria', 'alumno',)

    def __unicode__(self):
        return self.title

class Favorito(models.Model):
    asesoria = models.ForeignKey(Asesoria, on_delete=models.CASCADE)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('asesoria', 'alumno',)
