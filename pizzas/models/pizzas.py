import uuid

from django.db import models

from .ingredients import Ingredient


class Pizza(models.Model):
    """Pizza model."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to="images/pizzas/", null=True, blank=True)

    ingredients = models.ManyToManyField(Ingredient, related_name="pizzas")

    def __str__(self):
        return self.name
