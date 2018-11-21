from django.test import TestCase
from django.test import Client
from profesor.forms import *

class Setup_Class(TestCase):

    def setUp(self):
        self.profesor = User.objects.create(codigoUlima="12345678", password="1234")

class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = LoginForm(data={'codigoUlima': "12345678", 'password': "1234"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = LoginForm(data={'codigoUlima': "20141729", 'password': "12354"})
        self.assertFalse(form.is_valid())
