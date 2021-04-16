from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def test_home_page_view(self):

        response = self.client.get(reverse('home_page'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
