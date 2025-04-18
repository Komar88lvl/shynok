from django.test import TestCase, Client
from django.urls import reverse


DISH_TYPE_URL = reverse("kitchen:dish-type-list")

class PublicDishTypeTest(TestCase):
    def test_login_dish_type_list_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)
