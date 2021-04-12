from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UsersTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username='test_username',
            email='test@test.com',
            age=10,
            password='secret'
        )

    def test_user_signup_view(self):
        response = self.client.post(reverse('signup'), {
            'username': 'test2',
            'age': 10,
            'password': 'secret'
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 10)
