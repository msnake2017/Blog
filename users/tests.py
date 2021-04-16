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
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_user_signup_form(self):

        get_user_model().objects.create_user(
                username='test_username_2',
                email='test_email@tested.com',
                password='secret',
                age=20
            )
        self.assertEqual(get_user_model().objects.all().count(), 2)
        self.assertEqual(get_user_model().objects.all()[1].username,
                         'test_username_2')
        self.assertEqual(get_user_model().objects.all()[1].email,
                         'test_email@tested.com')
