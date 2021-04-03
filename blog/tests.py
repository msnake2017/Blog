from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username='test_user',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            author=self.user,
            title='test_title',
            body='test_body'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.author}', 'test_user')
        self.assertEqual(f'{self.post.title}', 'test_title')
        self.assertEqual(f'{self.post.body}', 'test_body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test_title')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        no_response = self.client.get(reverse('post_detail', args=[0]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test_body')
        self.assertTemplateUsed(response, 'blog/post_detail.html')

