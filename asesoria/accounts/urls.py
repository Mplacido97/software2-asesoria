from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [

    path('home/', views.home),
    path('register/', views.register, name='register'),
    path('', login ,{'template_name':'login.html'})

]
