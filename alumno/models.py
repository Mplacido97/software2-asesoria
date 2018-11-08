from django.db import models
import datetime
from django.contrib.auth.models import User
from  profesor.models import *
#from django.contrib.auth.model import User
# Create your models here.

#class UserProfile(models.Model):

#    USERS_TYPE = ('Alumno','Profesor')

    #user = models.OnetoOneField(User)
    #tipo = (models.chartField(max_legnth=10, choices = USERS_TYPE))
    #carrera = models.chartField(default=10)

class Alumno(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    codigoUlima  = models.CharField(max_length=20, unique=True)
    email  = models.CharField(max_length=30, unique=True)


    def __str__(self):
        return "PK: {}, Nombre: {}, Código: {}".format(self.pk, self.nombre, self.codigoUlima)

    @staticmethod
    def verify_user(codigoUlima, password):
        alumno = Alumno.objects.filter(codigoUlima=codigoUlima).first()
        return alumno != None and alumno.password == password, alumno

class Cita(models.Model):
    asesoria = models.ForeignKey(Asesoria, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    semana = models.IntegerField()
    finalizado = models.BooleanField(default=False)
    #PUEDE MEJORARSE
    tema = models.CharField(max_length=300)

    class Meta:
        unique_together = ('asesoria', 'alumno',)

    def __str__(self):
        return "Asesoria: {}, Alumno: {}".format(self.asesoria, self.alumno)


class Favorito(models.Model):
    asesoria = models.ForeignKey(Asesoria, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('asesoria', 'alumno',)

    def __str__(self):
        return "Asesoria: {}, Alumno: {}".format(self.asesoria, self.alumno)


class Comentario(models.Model):

    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    rate = models.IntegerField()
    comment = models.CharField(max_length = 200)
