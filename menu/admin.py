from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Dish, DishType, Ingredient, Cook


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", "specialization")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("years_of_experience", "specialization")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "years_of_experience",
                    "specialization",
                )
            },


        )
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price")
    search_fields = ("name",)
    list_filter = ("dish_type",)
    filter_horizontal = ("cooks", "ingredients")


admin.site.register(DishType)
admin.site.register(Ingredient)