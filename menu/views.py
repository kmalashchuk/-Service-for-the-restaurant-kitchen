from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView

from menu.models import Dish, Ingredient, DishType, Cook
from django.shortcuts import render

def index(request):
    return render(request, "menu/index.html")


class DishListView(generic.ListView):
    model = Dish


class DishDetailView(generic.DetailView):
    model = Dish
    context_object_name = "dish"


class DishCreateView(generic.CreateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "ingredients", "cooks"]
    success_url = reverse_lazy("menu:dish-list")
    template_name = "forms/dish_form.html"

class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "ingredients", "cooks"]
    success_url = reverse_lazy("menu:dish-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("menu:dish-list")


class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = "menu/ingredient_list.html"
    context_object_name = "ingredient_list"
    paginate_by = 10


class IngredientCreateView(generic.CreateView):
    model = Ingredient
    fields = ["name"]
    success_url = reverse_lazy("menu:ingredient-list")
    template_name = "forms/ingredient_form.html"

class IngredientUpdateView(generic.UpdateView):
    model = Ingredient
    fields = ["name"]
    success_url = reverse_lazy("menu:ingredient-list")


class IngredientDeleteView(generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("menu:ingredient-list")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "menu/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 10


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = ["name"]
    success_url = reverse_lazy("menu:dishtype-list")
    template_name = "forms/dishtype_form.html"


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = ["name"]
    success_url = reverse_lazy("menu:dishtype-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("menu:dishtype-list")


class CookListView(generic.ListView):
    model = Cook
    template_name = "menu/cook_list.html"
    context_object_name = "cook_list"
    paginate_by = 10


class CookDetailView(generic.DetailView):
    model = Cook
    context_object_name = "cook"
    template_name = "menu/cook_detail.html"


class CookCreateView(generic.CreateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience", "specialization"]
    success_url = reverse_lazy("menu:cook-list")
    template_name = "forms/cook_form.html"

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data["password"])
        return super().form_valid(form)


class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience", "specialization"]
    success_url = reverse_lazy("menu:cook-list")


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("menu:cook-list")
