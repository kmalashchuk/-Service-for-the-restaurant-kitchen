from django.test import TestCase
from django.urls import reverse
from menu.models import Dish, Ingredient, DishType, Cook
from django.contrib.auth import get_user_model

class PublicDishTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse("menu:index"))
        self.assertEqual(response.status_code, 200)

class PrivateDishTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="pass1234"
        )
        self.client.login(username="testuser", password="pass1234")

        self.ingredient1 = Ingredient.objects.create(name="Cheese")
        self.ingredient2 = Ingredient.objects.create(name="Dough")
        self.dish_type = DishType.objects.create(name="Pizza")
        self.cook = Cook.objects.create(username="cook1")

    def test_create_dish_with_multiple_ingredients(self):
        data = {
            "name": "Test Pizza",
            "dish_type": self.dish_type.id,
            "ingredients": [self.ingredient1.id, self.ingredient2.id],
            "cooks": [self.cook.id],
        }
        response = self.client.post(reverse("menu:dish-create"), data)
        self.assertEqual(response.status_code, 302)

        dish = Dish.objects.get(name="Test Pizza")
        self.assertEqual(dish.ingredients.count(), 2)
        self.assertEqual(dish.cooks.count(), 1)

    def test_dish_list_view(self):
        Dish.objects.create(name="Sample", dish_type=self.dish_type)
        response = self.client.get(reverse("menu:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample")
