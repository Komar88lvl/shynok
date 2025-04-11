from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import DishType, Dish, Cook


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "dish_type", "price",]
    list_filter = ["dish_type__name", ]
    search_fields = ["name", ]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (
        ("Qualification", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {
            "fields": ("first_name", "last_name", "email", "years_of_experience",)
        }),
    )


admin.site.register(DishType)
