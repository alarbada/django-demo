from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.product1 = Product.objects.create(
            title="Product 1",
            description="This is product 1",
            price=10.99
        )
        self.product2 = Product.objects.create(
            title="Product 2",
            description="This is product 2",
            price=20.99
        )

    def test_list_products(self):
        url = reverse("products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding="utf8"),
            [
                {"title": "Product 1", "description": "This is product 1", "price": 10.99},
                {"title": "Product 2", "description": "This is product 2", "price": 20.99},
            ]
        )

    def test_create_product(self):
        url = reverse("products")
        data = {
            "title": "New Product",
            "description": "This is a new product",
            "price": 15.99
        }
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.post(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
