from django.test import TestCase, Client

# Create your tests here.
def test_url_accordion(self):
            response = Client().get('/story7/')
            self.assertEquals(response.status_code, 200)

def test_template_accordion(self):
    response = Client().get('/story7/')
    self.assertTemplateUsed(response, 'accr.html')