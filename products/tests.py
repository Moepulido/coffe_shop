from django.test import TestCase
from django.urls import reverse
from django.utils.translation import override
from .models import Product


# Create your tests here.
class ProductListViewTest(TestCase):

    def test_should_return_200_in_all_languages(self):
        for lang in ["es", "en", "fr"]:
            with override(lang):
                url = reverse("product_list")
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(len(response.context["products"]), 0)

    def test_should_return_200_with_products_in_all_languages(self):
        Product.objects.create(
            name="Test Product",
            price=10.00,
            description="Test Description",
            available=True,
        )
        for lang in ["es", "en", "fr"]:
            with override(lang):
                url = reverse("product_list")
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.context["products"].count(), 1)
