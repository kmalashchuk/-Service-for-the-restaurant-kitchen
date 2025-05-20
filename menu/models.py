from django.db import models

class DishType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


class Dish(models.Model):
    name = models.CharField(max_length=100)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)



class Cookie(models.Model):
    name = models.CharField(max_length=100)
