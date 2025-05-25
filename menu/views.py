from django.views.generic import DetailView, UpdateView, DeleteView, ListView

from menu.models import Dish

class DishListView(ListView):
    model = Dish

class DishDetailView(DetailView):
    model = Dish
    context_object_name = "dish"

class DishUpdateView(UpdateView):
    model = Dish
    fields = ["__all__"]
    success_url = "menu:dish-list"

class DishDeleteView(DeleteView):
    model = Dish
    success_url = "menu:dish-list"