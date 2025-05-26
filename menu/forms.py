from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Dish, Cook, Ingredient, DishType


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "ingredients", "cooks"]
        widgets = {
            "ingredients": forms.CheckboxSelectMultiple(),
            "cooks": forms.CheckboxSelectMultiple(),
        }


class CookCreateForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ["username", "first_name", "last_name", "years_of_experience", "specialization"]


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["first_name", "last_name", "years_of_experience", "specialization"]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]
