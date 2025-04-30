from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})


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
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="type_dishes",
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes",
    )

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self):
        return f"{self.name} {self.price}"
