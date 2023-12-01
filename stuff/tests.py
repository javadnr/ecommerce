from django.test import TestCase
from .models import Product,Comment
from django.urls import reverse
from django.contrib.auth import get_user_model

class ProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(username='john',email = 'john@email.com',password = '12345678')
        cls.product = Product.objects.create(name = 'iphone16',price = '1000.00',discription = 'nice one')
        cls.comment = Comment.objects.create(author = cls.user, post = cls.product, body = 'too expensive')
        
    def test_book_listing(self):
        self.assertEqual(f"{self.product.name}", "iphone16")
        self.assertEqual(f"{self.product.price}", "1000.00")
        self.assertEqual(f"{self.product.discription}", "nice one")
        
    def test_book_list_view(self):
        response = self.client.get(reverse("list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "iphone16")
        self.assertTemplateUsed(response, "stuff/list.html")
        
    def test_book_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get("/detail/asidlasj/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "too expensive")
        self.assertContains(response, "iphone16")
        self.assertTemplateUsed(response, "stuff/detail.html")