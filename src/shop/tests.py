from django.test import TestCase


class ShopTest(TestCase):
    def test_index(self):
        result = self.client.get('/shop/')
        self.assertEqual(result.status_code, 200)
