from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType

DISH_TYPE_URL = reverse("kitchen:dish-type-list")


class PublicDishTypeTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="testdishtype")

    def test_login_dish_type_list_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_dish_type_detail_required(self):
        url = reverse(
            "kitchen:dish-type-detail",
            args=[self.dish_type.id]
        )
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)
