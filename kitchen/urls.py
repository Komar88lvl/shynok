from django.urls import path

from kitchen.views import (
       index,
       DishTypeListView,
       DishTypeDetailView,
       CookListView,
       DishListView,

)

urlpatterns = [
       path("", index, name="index"),

       path(
              "dish-types/",
              DishTypeListView.as_view(),
              name="dish-type-list"
       ),
       path(
              "dish-types/<int:pk>/",
              DishTypeDetailView.as_view(),
              name="dish-type-detail"
       ),

       path(
              "cooks/",
              CookListView.as_view(),
              name="cook-list"
       ),

       path(
              "dishes/",
              DishListView.as_view(),
              name="dish-list"
       ),


]

app_name = "kitchen"
