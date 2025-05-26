from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.index, name="index"),
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>", views.DishDetailView.as_view(), name="dish-detail"),
    path("dishes/update/", views.DishUpdateView.as_view(), name="dish-update"),
    path("dishes/delete/", views.DishDeleteView.as_view(), name="dish-delete"),
    path("dishes/create/", views.DishCreateView.as_view(), name="dish-create"),


    # INGREDIENT URLs
    path("ingredients/", views.IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", views.IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/update/", views.IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/<int:pk>/delete/", views.IngredientDeleteView.as_view(), name="ingredient-delete"),

    # DISHTYPE URLs
    path("dishtypes/", views.DishTypeListView.as_view(), name="dishtype-list"),
    path("dishtypes/create/", views.DishTypeCreateView.as_view(), name="dishtype-create"),
    path("dishtypes/<int:pk>/update/", views.DishTypeUpdateView.as_view(), name="dishtype-update"),
    path("dishtypes/<int:pk>/delete/", views.DishTypeDeleteView.as_view(), name="dishtype-delete"),

    #Cook URLs
    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    path("cooks/create/", views.CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>", views.CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/", views.CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", views.CookDeleteView.as_view(), name="cook-delete"),
    path("dishes/<int:pk>/toggle-assign/", views.toggle_assign_to_dish, name="toggle-assign-to-dish"),
]
