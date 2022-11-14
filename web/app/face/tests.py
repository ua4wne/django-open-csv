from django.test import TestCase
from django.test import Client
from django.urls import reverse
from face.models import Url, BoundingBox


class FaceTest(TestCase):
    """Test our app"""

    def setUp(self):
        self.client = Client()

    def test_delete_item(self):
        """Test deleting Url with bounding box"""
        url = Url.objects.create(image_url='https://m-strana.ru/upload/resize_cache/iblock/6c1/270_280_1/6c1710eaba574c26d69dc7c874706025.png')
        BoundingBox.objects.create(top=1, bottom=1, right=1, left=1, image=url)

        urls = Url.objects.all()
        bbs = BoundingBox.objects.all()

        self.client.get(reverse('delete', kwargs={'url_id': url.id}))
        urls = Url.objects.all()
        bbs = BoundingBox.objects.all()

        self.assertEqual(len(urls), 0)
        self.assertEqual(len(bbs), 0)
