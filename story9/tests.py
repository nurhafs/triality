from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import resolve
from .views import specialPage

# Create your tests here.
class TesSession(TestCase):
    def tes_url_page(self):
        response = Client().get('/special/')
        self.assertEquals(response.status_code, 200)

    def tes_url_login(self):
        response = Client().get('/special/login')
        self.assertEquals(response.status_code, 200)

    def tes_url_signup(self):
        response = Client().get('/special/signup/')
        self.assertEquals(response.status_code, 200)
    
    def test_url_logout(self):
        response = Client().get('/special/logout/')
        self.assertEquals(response.status_code, 200)

    def test_template_page(self):
        response = Client().get('/special/')
        self.assertTemplateUsed('spec.html')
    
    def test_template_login(self):
        response = Client().get('/special/login')
        self.assertTemplateUsed('login.html')

    def test_template_signup(self):
        response = Client().get('/special/signup/')
        self.assertTemplateUsed('signup.html')

    def test_template_logout(self):
        response = Client().get('/special/logout/')
        self.assertTemplateUsed('logged_out.html')
    
    def test_view_page(self):
        response = resolve('/special/')
        self.assertEquals(response.func, specialPage)
    
    def test_create_user(self):
        User.objects.create_user(username='haji', email='haji@network', password='terbang')
        exist = User.objects.filter(username='haji').exists()
        self.assertTrue(exist)