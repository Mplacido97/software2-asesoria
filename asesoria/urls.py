
from django.contrib import admin
from django.urls import path, include
from asesoria import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('alumno/', include('alumno.urls', namespace='alumno')),
    path('profesor/', include('profesor.urls', namespace='profesor')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
