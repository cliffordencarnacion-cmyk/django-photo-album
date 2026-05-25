from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Album

User = get_user_model()


class AlbumViewsTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='admin', password='password123', is_staff=True)
        self.album = Album.objects.create(title='Test Album', description='A test album', owner=self.owner)

    def test_album_list_status_code(self):
        response = self.client.get(reverse('album-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Album')

    def test_album_detail_status_code(self):
        response = self.client.get(reverse('album-detail', kwargs={'pk': self.album.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A test album')

    def test_album_create_requires_login(self):
        response = self.client.get(reverse('album-add'))
        self.assertRedirects(response, '/accounts/login/?next=/albums/add/')

    def test_album_create_with_admin_user(self):
        self.client.login(username='admin', password='password123')
        response = self.client.post(reverse('album-add'), {'title': 'New Album', 'description': 'Created by admin'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Album.objects.filter(title='New Album').exists())
