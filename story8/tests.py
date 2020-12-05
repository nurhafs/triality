from django.test import TestCase, Client
from django.urls import resolve
from .views import findbooks, olah_data
# Create your tests here.

class TestCariBuku(TestCase):
    def test_url_caribuku(self):
        response = Client().get('/books/')
        self.assertEquals(response.status_code, 200)
    
    def test_url2_caribuku(self):
        response = Client().get('/books/data/')
        self.assertEquals(response.status_code, 200)

    def test_template_caribuku(self):
        response = Client().get('/books/')
        self.assertTemplateUsed(response, 'findbk.html')

    def test_view_caribuku(self):
        response = resolve('/books/')
        self.assertEquals(response.func, findbooks)

    def test_view2_caribuku(self):
        response = resolve('/books/data/?q=toy%20world')
        self.assertEquals(response.func, olah_data)