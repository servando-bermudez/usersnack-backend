from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Order, Item


def reverse_foreignkey_change_links(
    model, get_instances, description=None, get_link_html=None, empty_text="(None)"
):
    if not description:
        description = model.__name__ + "(s)"

    def model_change_link_function(_, obj):
        instances = get_instances(obj)
        if instances.count() == 0:
            return empty_text
        output = ""
        links = []
        for instance in instances:
            change_url = reverse(
                "admin:%s_change" % model._meta.db_table, args=(instance.id,)
            )
            links.append('<a href="%s">%s</a>' % (change_url, instance.__str__()))
        return format_html("</br></br>".join(links))

    model_change_link_function.short_description = description
    model_change_link_function.allow_tags = True
    return model_change_link_function


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "total", "created_at")
    ordering = ("-created_at",)
    fields = ("created_at", "items", "total")
    readonly_fields = (
        "total",
        "items",
    )

    def items(self, obj):
        return reverse_foreignkey_change_links(
            model=Order,
            get_instances=lambda obj: obj.items.all(),
            description="Items",
        )(self, obj)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "total", "quantity", "pizza", "order")
    ordering = ("-order",)
    fields = (
        "quantity",
        "pizza",
        "order",
        "extras",
        "extras_readonly",
    )
    readonly_fields = (
        "extras_readonly",
        "total",
    )
    list_select_related = True

    def extras_readonly(self, obj):
        return reverse_foreignkey_change_links(
            model=Item,
            get_instances=lambda obj: obj.extras.all(),
            description="Extras",
        )(self, obj)
