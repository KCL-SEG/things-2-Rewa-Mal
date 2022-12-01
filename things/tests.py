from django.test import TestCase
from things.forms import ThingForm

# Create your tests here.
class ThingFormTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.input = {
            'name': 'Thing',
            'description': "Thing's description",
            'quantity': 2
        }
    
    def test_valid_form(self):
        form = ThingForm(data=self.input)
        self.assertTrue(form.is_valid())

class HomeViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('home')

    def test_get_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')