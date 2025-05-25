from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.index, name="index"),
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>", views.DishDetailView.as_view(), name="dish-detail"),
    path("dishes/update/", views.DishUpdateView.as_view(), name="dish-update"),
    path("dishes/delete/", views.DishDeleteView.as_view(), name="dish-delete"),
]
