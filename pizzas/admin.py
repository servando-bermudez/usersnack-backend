from django.contrib import admin

from .models import Extra, Ingredient, Pizza


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    search_fields = ("name",)


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)
    filter_horizontal = ("ingredients",)
    list_filter = ("ingredients",)
    ordering = ("name",)
    autocomplete_fields = ("ingredients",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "price",
                    "ingredients",
                    "img",
                )
            },
        ),
    )
    search_fields = ("name",)
    list_per_page = 50
    list_select_related = True
    save_on_top = True
