from django.db import models

# Create your models here.


class Profesor(models.Model):

    state_options = (
        ('Disponible', 'Disponible'),
        ('Ocupado', 'Ocupado'),
        ('Ausente', 'Ausente'),
        ('No disponible', 'No disponible'),
    )

    nombrepProfesor = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    codigoUlima  = models.CharField(max_length=20, unique=True)
    email  = models.CharField(max_length=30, unique=True)
    state = models.CharField(max_length=20, choices=state_options)

    def __str__(self):
        return "PK: {}, Nombre: {}, Código ULima: {}".format(self.pk, self.nombrepProfesor, self.codigoUlima)

    @staticmethod
    def verify_user(codigoUlima, password):
        profesor = Profesor.objects.filter(codigoUlima=codigoUlima).first()
        return profesor != None and profesor.password == password, profesor

class Curso(models.Model):
    nombreCurso = models.CharField(max_length=50)
    seccion = models.IntegerField()
    codProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return "Nombre del Curso: {}".format(self.nombreCurso)

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
    codCurso= models.ForeignKey(Curso, on_delete=models.CASCADE,)
    fechaAsesoria = models.CharField(max_length=12, choices=dia_semana)
    horaInicio = models.TimeField(default="12:00")
    lugar = models.ForeignKey(Salon, on_delete=models.CASCADE)

    def __str__(self):
        return "PK: {}, Profesor: {}, Curso".format(self.pk, self.codProfesor, self.codCurso)
