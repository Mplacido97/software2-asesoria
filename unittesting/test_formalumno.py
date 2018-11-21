from django.test import TestCase
from django.test import Client
from alumno.forms import *

class Setup_Class(TestCase):

    def setUp(self):
        self.alumno = User.objects.create(codigoUlima="20141729", password="1234")

class alumno_Form_Test(TestCase):

    # Valid Form Data
    def test_alumnoForm_valid(self):
        form = LoginForm(data={'codigoUlima': "20141729", 'password': "1234"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_alumnoForm_invalid(self):
        form = LoginForm(data={'codigoUlima': "20141729", 'password': "12354"})
        self.assertFalse(form.is_valid())
