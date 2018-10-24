
from django.contrib import admin
from django.urls import path, include
from asesoria import views

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('alumno/', include('alumno.urls', namespace='alumno')),
    path('profesor/', include('profesor.urls', namespace='profesor')),
]
