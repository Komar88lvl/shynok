from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType

DISH_URL = reverse("kitchen:dish-list")


class PublicDishTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_detail_required(self):
        dish_type = DishType.objects.create(name="test")
        dish = Dish.objects.create(
            name="testdish",
            dish_type=dish_type,
            price=14.20,
        )
        url = reverse(
            "kitchen:dish-detail",
            args=[dish.id]
        )
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

        self.dish_type = DishType.objects.create(
            name="test",
        )

    def test_retrieve_dishes(self):
        Dish.objects.create(
            name="salad_test",
            dish_type=self.dish_type,
            price=10.50,
        )
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")
