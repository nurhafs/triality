from django.test import TestCase

# Create your tests here.
def test_url_kegiatan(self):
            response = Client().get('/story7/')
            self.assertEquals(response.status_code, 200)

def test_template_kegiatan(self):
    response = Client().get('/story7/')
    self.assertTemplateUsed(response, 'accr.html')