from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import DishType, Dish, Cook


class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "dish_type", "price",]
    list_filter = ["dish_type__name", ]
    search_fields = ["name", ]


admin.site.register(DishType)
admin.site.register(Dish, DishAdmin)
admin.site.register(Cook, UserAdmin)
