from django.urls import path
from . import views
from django.contrib.auth.views import login


urlpatterns = [

    path('home/', views.home),
    path('lista_profesores/', views.lista_profesores),
    path('calendario/', views.calendar),
    path('favoritos/', views.favoritos),
    path('historial/', views.historial),
    path('register/', views.register, name='register'),
    path('login/', login ,{'template_name':'login.html'}),




    path('agregar_cita/(?P<codAsesoria>\w+)/', views.agregar_cita, name="agregar_cita"),
    path('agregar_favorito/(?P<codAsesoria>\w+)/', views.agregar_favorito, name="agregar_favorito"),
    path('eliminar_favorito/(?P<codFavorito>\w+)/', views.eliminar_favorito, name="eliminar_favorito")

]
