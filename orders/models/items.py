import uuid

from django.db import models

from orders.models import Order
from pizzas.models import Pizza, Extra


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.PositiveIntegerField(default=1)

    # Relationship
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    extras = models.ManyToManyField(Extra, related_name="items", blank=True)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return f"{self.pizza} - {self.quantity} ({self.order})"

    @property
    def total(self):
        return (
            self.pizza.price + sum(extra.price for extra in self.extras.all())
        ) * self.quantity
