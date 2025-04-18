from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


COOK_URL = reverse("kitchen:cook-list")


class PublicCookTest(TestCase):
    def test_login_cook_list_required(self):
        res = self.client.get(COOK_URL)
        self.assertNotEqual(res.status_code, 200)
