from django.urls import path
from . import views
from django.contrib.auth.views import login


app_name = 'alumno'
urlpatterns = [

    path('home/', views.home, name="home"),
    path('lista_profesores/', views.lista_profesores, name="lista_profesores"),
    path('calendario/(?P<num_semana>\d+)/', views.calendar, name="calendario"),
    path('favoritos/', views.favoritos, name="favoritos"),
    path('historial/', views.historial, name="historial"),
    path('register/', views.register, name='register'),
    path('login/',  views.login, name='login'),
    path('log_out/',  views.log_out, name='log_out'),



    path('perfil_profesor/(?P<pk_profesor>\w+)/', views.perfil_profesor, name="perfil_profesor"),
    path('agregar_cita/(?P<asesoria>\w+)/', views.agregar_cita, name="agregar_cita"),
    path('agregar_favorito/(?P<asesoria>\w+)/', views.agregar_favorito, name="agregar_favorito"),
    path('eliminar_favorito/(?P<favorito>\w+)/', views.eliminar_favorito, name="eliminar_favorito"),
    path('eliminar_cita/(?P<cita>\w+)/', views.eliminar_cita, name="eliminar_cita"),
    path('finalizar_cita/(?P<cita>\w+)/', views.finalizar_cita, name="finalizar_cita"),

]
