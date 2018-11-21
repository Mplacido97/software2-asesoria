from django.test import TestCase
from django.test import Client
from .forms import *   # import all forms
from profesor.models import *
from django.urls import reverse

class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="20141729", first_name="juan", last_name="court", email="juancourt@gmail.com",password1="1234",password2="1234")

class alumno_Views_Test(SetUp_Class):

    def test_home_view(self):
        user_login = self.client.login(email="juancourt@gmail.com", password="1234")
        self.assertTrue(user_login)
        response = self.client.get('home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class profesorListViewTest(TestCase):
nombrepProfesor = models.CharField(max_length=60)
password = models.CharField(max_length=20)
codigoUlima  = models.CharField(max_length=20, unique=True)
email  = models.CharField(max_length=30, unique=True)
state = models.CharField(max_length=20, choices=state_options)
image = models.ImageField(upload_to="profesores/")

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        profesores = 13
        for author_num in range(profesores):
            Profesor.objects.create(nombrepProfesor='Christian %s' % author_num, password = '1234 %s' % author_num,codigoUlima= '20141729 %s' % author_num,email= 'chris@gmail.com %s' % author_num,state= 'Disponible %s' % author_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('alumno/Tony/lista_profesores.html')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('lista_profesores'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'alumno/Tony/lista_profesores.html')

    def test_pagination_is_false(self):
        resp = self.client.get(reverse('lista_profesores'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == False)
