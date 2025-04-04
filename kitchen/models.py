from django.db import models
from django.contrib.auth.models import AbstractUser


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False,
    )
    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    description = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.SET_DEFAULT,
        default="some_type",
        related_name="type_dishes",
    )
    cooks = models.ManyToManyField(
        Cook,
        related_name="dishes",
    )

    def __str__(self):
        return f"{self.name} {self.price}"
