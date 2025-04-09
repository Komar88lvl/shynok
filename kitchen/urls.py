from django.urls import path

from kitchen.views import (
       index,
       DishTypeListView,
       DishListView,
       CookListView,
       DishTypeDetailView,
)

urlpatterns = [
       path("", index, name="index"),

       path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
       path(
              "dish-types/<int:pk>/",
              DishTypeDetailView.as_view(),
              name="dish-type-detail"
       ),

       path("dishes/", DishListView.as_view(), name="dish-list"),

       path("cooks/", CookListView.as_view(), name="cook-list"),
]

app_name = "kitchen"
