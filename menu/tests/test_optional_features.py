from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from menu.models import Dish, Ingredient, DishType


class ToggleAssignToDishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="cook1", password="testpass123", years_of_experience=5
        )
        self.dish_type = DishType.objects.create(name="Soup")
        self.dish = Dish.objects.create(
            name="Borscht", description="Beetroot soup", price=5.5, dish_type=self.dish_type
        )
        self.client.login(username="cook1", password="testpass123")

    def test_toggle_assign(self):
        url = reverse("menu:toggle-assign-to-dish", args=[self.dish.id])

        # Assign user to dish
        self.client.post(url)
        self.assertIn(self.user, self.dish.cooks.all())

        # Unassign user from dish
        self.client.post(url)
        self.assertNotIn(self.user, self.dish.cooks.all())


class IndexViewTest(TestCase):
    def setUp(self):
        DishType.objects.create(name="Main")
        Ingredient.objects.create(name="Salt")
        get_user_model().objects.create_user(
            username="chef", password="testpass123", years_of_experience=10
        )

    def test_index_view_counts(self):
        response = self.client.get(reverse("menu:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ingredients: 1")
        self.assertContains(response, "Dish types: 1")
        self.assertContains(response, "Cooks: 1")


class DishCreateTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Salad")
        self.ingredient1 = Ingredient.objects.create(name="Lettuce")
        self.ingredient2 = Ingredient.objects.create(name="Tomato")
        self.user = get_user_model().objects.create_user(
            username="chef", password="testpass123", years_of_experience=2
        )
        self.client.login(username="chef", password="testpass123")

    def test_create_dish_with_multiple_ingredients(self):
        url = reverse("menu:dish-create")
        data = {
            "name": "Fresh Salad",
            "description": "Healthy and green",
            "price": 3.99,
            "dish_type": self.dish_type.id,
            "ingredients": [self.ingredient1.id, self.ingredient2.id],
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        dish = Dish.objects.get(name="Fresh Salad")
        self.assertIn(self.ingredient1, dish.ingredients.all())
        self.assertIn(self.ingredient2, dish.ingredients.all())
