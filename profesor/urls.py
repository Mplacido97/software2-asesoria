from django.urls import path
from . import views
from django.contrib.auth.views import login


app_name = 'profesor'
urlpatterns = [

    path('home/', views.home),
    path('login/', views.login),
    path('citas/', views.citas),
    path('calendario/', views.calendar),
    path('historial/', views.historial),
    path('log_out/',  views.log_out, name='log_out'),
    path('change_state/',  views.change_state),


    path('perfil_profesor/', views.perfil_profesor, name="perfil_profesor"),
    path('eliminar_cita/(?P<cita>\w+)/', views.eliminar_cita, name="eliminar_cita"),

]
