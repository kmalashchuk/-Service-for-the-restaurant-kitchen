from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView

from menu.models import Dish, Ingredient, DishType
from django.shortcuts import render

def index(request):
    return render(request, "menu/index.html")

class DishListView(generic.ListView):
    model = Dish

class DishDetailView(generic.DetailView):
    model = Dish
    context_object_name = "dish"

class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = ["__all__"]
    success_url = reverse_lazy("menu:dish-list")

class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("menu:dish-list")

class DishCreateView(generic.CreateView):
    model = Dish
    fields = ["__all__"]
    success_url = reverse_lazy("menu:dish-list")

class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = ("menu/ingredient_list.html")
    context_object_name = "ingredient_list"
    paginate_by = 10

class IngredientCreateView(generic.CreateView):
    model = Ingredient
    fields = ["__all__"]
    success_url = reverse_lazy("menu:ingredient-list")

class IngredientUpdateView(generic.UpdateView):
    model = Ingredient
    fields = ["__all__"]
    success_url = reverse_lazy("menu:ingredient-list")

class IngredientDeleteView(generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("menu:ingredient-list")

class DishTypeListView(generic.ListView):
    model = DishType
    fields = ["__all__"]
    template_name = ("menu/dish_type_list.html")
    context_object_name = "dish_type_list"
    paginate_by = 10

class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = ["__all__"]
    success_url = reverse_lazy("menu:dishtype-list")

class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = ["__all__"]
    success_url = reverse_lazy("menu:dishtype-list")

class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("menu:dishtype-list")