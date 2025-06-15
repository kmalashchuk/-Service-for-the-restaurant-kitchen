from django.test import TestCase
from django.urls import reverse
from menu.models import DishType, Ingredient, Cook
from django.contrib.auth import get_user_model


class CrudTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="pass1234"
        )
        self.client.login(username="testuser", password="pass1234")

    # === INGREDIENT ===

    def test_create_ingredient(self):
        response = self.client.post(reverse("menu:ingredient-create"), {"name": "Tomato"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Ingredient.objects.filter(name="Tomato").exists())

    def test_update_ingredient(self):
        ingredient = Ingredient.objects.create(name="OldName")
        response = self.client.post(
            reverse("menu:ingredient-update", args=[ingredient.id]),
            {"name": "NewName"}
        )
        self.assertEqual(response.status_code, 302)
        ingredient.refresh_from_db()
        self.assertEqual(ingredient.name, "NewName")

    def test_delete_ingredient(self):
        ingredient = Ingredient.objects.create(name="DeleteMe")
        response = self.client.post(
            reverse("menu:ingredient-delete", args=[ingredient.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Ingredient.objects.filter(name="DeleteMe").exists())

    # === DISH TYPE ===

    def test_create_dish_type(self):
        response = self.client.post(reverse("menu:dishtype-create"), {"name": "Soup"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(DishType.objects.filter(name="Soup").exists())

    def test_update_dish_type(self):
        dt = DishType.objects.create(name="OldType")
        response = self.client.post(
            reverse("menu:dishtype-update", args=[dt.id]),
            {"name": "NewType"}
        )
        self.assertEqual(response.status_code, 302)
        dt.refresh_from_db()
        self.assertEqual(dt.name, "NewType")

    def test_delete_dish_type(self):
        dt = DishType.objects.create(name="DeleteType")
        response = self.client.post(
            reverse("menu:dishtype-delete", args=[dt.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(DishType.objects.filter(name="DeleteType").exists())

    # === COOK ===

    def test_create_cook(self):
        response = self.client.post(reverse("menu:cook-create"), {
            "username": "cook2",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(get_user_model().objects.filter(username="cook2").exists())

    def test_update_cook(self):
        cook = get_user_model().objects.create_user(username="cook3", password="pass")
        response = self.client.post(
            reverse("menu:cook-update", args=[cook.id]),
            {"username": "updatedcook", "password": "pass"}
        )
        self.assertEqual(response.status_code, 302)
        cook.refresh_from_db()
        self.assertEqual(cook.username, "updatedcook")

    def test_delete_cook(self):
        cook = get_user_model().objects.create_user(username="deletecook", password="pass")
        response = self.client.post(reverse("menu:cook-delete", args=[cook.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(get_user_model().objects.filter(username="deletecook").exists())
