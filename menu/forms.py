from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Dish, Cook, Ingredient, DishType


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "ingredients", "cooks"]
        widgets = {
            "ingredients": forms.SelectMultiple(attrs={"size": 10}),
            "cooks": forms.SelectMultiple(attrs={"size": 5}),
        }


class CookCreateForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "username",
            "first_name",
            "last_name",
            "years_of_experience",
            "specialization",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
            "specialization"
        )


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class DishSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search dish by name"})
    )

class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search type by name"})
    )

class CookSearchForm(forms.Form):
    username = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search cook by username"})
    )

class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search ingredient by name"})
    )
