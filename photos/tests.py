from django.test import TestCase
from django.urls import reverse

class PhotoAppTest(TestCase):

    def test_photo_list_view_by_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_photo_list_view_by_url_name(self):
        response = self.client.get(reverse('photo_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_photo_detail_view_by_url(self):
        response = self.client.get('/2/')
        self.assertEqual(response.status_code, 200)
    
    def test_photo_detail_view_by_url_name(self):
        response = self.client.get(reverse('photo_detail', args=['3']))
        self.assertEqual(response.status_code, 200)