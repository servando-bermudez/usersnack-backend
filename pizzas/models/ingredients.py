import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractIngredient(models.Model):
    """Abstract ingredient model."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Ingredient Name"), max_length=255, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Ingredient(AbstractIngredient):
    """Ingredient model."""

    class Meta:
        verbose_name = _("Ingredient")
        verbose_name_plural = _("Ingredients")


class Extra(AbstractIngredient):
    """Extra model."""

    price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = _("Extra")
        verbose_name_plural = _("Extras")

    def __str__(self):
        return self.name
