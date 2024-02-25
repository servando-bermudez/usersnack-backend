import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    """Order model."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(_("Name"), max_length=255)
    address = models.CharField(_("Address"), max_length=255)

    created_at = models.DateTimeField(_("Created At"), default=timezone.now)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"Order {self.id} - {self.created_at}"

    @property
    def total(self):
        return sum(item.total for item in self.items.all())
