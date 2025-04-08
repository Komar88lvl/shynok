from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kitchen.models import Cook, DishType, Dish


def index(request: HttpRequest) -> HttpResponse:
    num_cooks = Cook.objects.count()
    num_type_dishes = DishType.objects.count()
    num_dishes = Dish.objects.count()
    context = {
        "num_cooks": num_cooks,
        "num_type_dishes": num_type_dishes,
        "num_dishes": num_dishes,
    }
    return render(request, "kitchen/index.html", context=context)