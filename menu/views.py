from itertools import product

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView

from menu.forms import DishSearchForm, DishTypeSearchForm, CookSearchForm, IngredientSearchForm, CookCreateForm, \
    DishForm
from menu.models import Dish, Ingredient, DishType, Cook
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def index(request):

    num_cooks = Cook.objects.count()
    num_dish = Dish.objects.count()
    num_dish_type = DishType.objects.count()
    products = serialize("json", Dish.objects.all(), fields=("name", "price"))
    num_dishes_assigned = 0

    if request.user.is_authenticated:
        num_dishes_assigned = request.user.dishes.count()

    context = {
        "num_cooks": num_cooks,
        "num_dish": num_dish,
        "num_dish_type": num_dish_type,
        "num_dishes_assigned": num_dishes_assigned,
        "products": products,
    }
    return render(request, "menu/index.html", context=context)


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 10
    queryset = Dish.objects.select_related("dish_type").prefetch_related("cooks")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name:
                return self.queryset.filter(name__icontains=name)
        return self.queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    context_object_name = "dish"


class DishCreateView(generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("menu:dish-list")
    template_name = "forms/dish_form.html"

    def form_valid(self, form):
        prise = form.cleaned_data["price"]
        if prise < 1.00:
            form.add_error("price", "Price must be greater than or equal to 1.00")
            return self.form_invalid(form)
        return super().form_valid(form)

class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "ingredients", "cooks"]
    success_url = reverse_lazy("menu:dish-list")
    template_name = "forms/dish_form.html"

class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("menu:dish-list")


class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = "menu/ingredient_list.html"
    context_object_name = "ingredient_list"
    paginate_by = 10
    queryset = Ingredient.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = IngredientSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = IngredientSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name:
                return self.queryset.filter(name__icontains=name)
        return self.queryset

class IngredientCreateView(generic.CreateView):
    model = Ingredient
    fields = ["name"]
    success_url = reverse_lazy("menu:ingredient-list")
    template_name = "forms/ingredient_form.html"

class IngredientUpdateView(generic.UpdateView):
    model = Ingredient
    fields = ["name"]
    success_url = reverse_lazy("menu:ingredient-list")
    template_name = "forms/ingredient_form.html"


class IngredientDeleteView(generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("menu:ingredient-list")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "menu/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 10
    queryset = DishType.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name:
                return self.queryset.filter(name__icontains=name)
        return self.queryset


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = ["name"]
    success_url = reverse_lazy("menu:dishtype-list")
    template_name = "forms/dish_type_form.html"


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = ["name"]
    success_url = reverse_lazy("menu:dishtype-list")
    template_name = "forms/dish_type_form.html"

class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("menu:dishtype-list")


class CookListView(generic.ListView):
    model = Cook
    template_name = "menu/cook_list.html"
    context_object_name = "cook_list"
    paginate_by = 10
    queryset = Cook.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(initial={"username": username})
        return context

    def get_queryset(self):
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if username:
                return self.queryset.filter(username__icontains=username)
        return self.queryset

class CookDetailView(generic.DetailView):
    model = Cook
    context_object_name = "cook"
    template_name = "menu/cook_detail.html"


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreateForm
    success_url = reverse_lazy("menu:cook-list")
    template_name = "forms/cook_form.html"


class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience", "specialization"]
    success_url = reverse_lazy("menu:cook-list")
    template_name = "forms/cook_form.html"

class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("menu:cook-list")


@login_required
def toggle_assign_to_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    cook = request.user

    if cook in dish.cooks.all():
        dish.cooks.remove(cook)
    else:
        dish.cooks.add(cook)

    return redirect("menu:dish-detail", pk=pk)
