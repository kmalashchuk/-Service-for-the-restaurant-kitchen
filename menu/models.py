from django.contrib.auth.models import AbstractUser, User
from django.db import models

class DishType(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ingredients"
        ordering = ["name"]
        verbose_name="Ingredient"


class Dish(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField("Cook", related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "dishes"
        verbose_name = "dish"


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)
    specialization = models.CharField(
        max_length=255,
        blank=True,
        help_text="Specialization of the cook",
    )

    def __str__(self):
       return f"{self.username} ({self.first_name} {self.last_name})"

    class Meta:
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"
        ordering = ("-years_of_experience",)