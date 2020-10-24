from django.test import TestCase, Client
from .models import Activity, Participant
from .forms import Act_Form, Par_Form

# Create your tests here.
class TestActivity(TestCase):
        def test_url_kegiatan(self):
            response = Client().get('/activity/')
            self.assertEquals(response.status_code, 200)

        def test_template_kegiatan(self):
            response = Client().get('/activity/')
            self.assertTemplateUsed(response, 'kegiatan.html')

        def test_url_addpeserta(self):
            k = Activity.objects.create(actname="bobo")
            response = Client().get('/activity/peserta/1')
            self.assertEquals(response.status_code, 200)

        def test_template_addpeserta(self):
            new_act = Activity.objects.create(actname="mancing")
            response = Client().get('/activity/peserta/1')
            self.assertTemplateUsed(response, 'people.html')
        
        def test_act_can_create_model(self):
            new_act = Activity.objects.create(actname = "Berenang di jagir")
            all_act = Activity.objects.all().count()
            self.assertEqual(all_act, 1)

        def test_par_can_create_model(self):
            new_act = Activity.objects.create(actname="tendang")
            new_par = Participant.objects.create(name="Doni", contact_number="089673489294", activity=new_act)
            all_par = Participant.objects.all().count()
            self.assertEqual(all_par, 1)

        def test_par_form_elements(self):
            new_act = Activity.objects.create(actname="tendang")
            response = Client().get('/activity/peserta/1')
            returned_html = response.content.decode('utf8')
            self.assertIn("Input your profile", returned_html)
            self.assertIn("Name", returned_html)
            self.assertIn("Contact number", returned_html)

        def test_act_form_elements(self):
            response = Client().get('/activity/')
            returned_html = response.content.decode('utf8')
            self.assertIn("Input your activity", returned_html)
            self.assertIn("Name", returned_html)
            self.assertIn("Submit", returned_html)
       
        def test_act_form_validation_for_blank_items(self):
            form = Act_Form(data={'actname': ''})
            self.assertFalse(form.is_valid())
            self.assertEqual(
                form.errors['actname'],
                ["This field is required."])
        
        # def test_par_form_validation_for_blank_items(self):
        #     form = Par_Form(data={'activity': '', 'name': '', 'contact_number':''})
        #     self.assertFalse(form.is_valid())
        #     self.assertEqual(
        #         form.errors['activity', 'name', 'contact_number'],
        #         ["This field is required."])



     
