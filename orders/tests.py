from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings


class MyOrderViewTest(TestCase):

    def test_no_logged_user_should_redirect(self):
        url = reverse("orders:my_order")
        response = self.client.get(url)
        expected_url = f"{settings.LOGIN_URL}?next={url}"
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, expected_url)

    def test_logged_user_should_redirect(self):
        url = reverse("orders:my_order")
        user = get_user_model().objects.create(username="testuser")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
