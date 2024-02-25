from rest_framework import serializers

from orders.models import Order
from orders.serializers import ItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    total = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "items",
            "name",
            "address",
            # Read-only fields
            "total",
        )
        read_only_fields = ("total",)

    def create(self, validated_data):
        items_data = validated_data.pop("items")

        order = Order.objects.create(**validated_data)

        self.context["order"] = order

        for item_data in items_data:
            item_data["order"] = order

            item_serializer = ItemSerializer(data=item_data, context=self.context)

            item_serializer.is_valid(raise_exception=True)

            item = item_serializer.save()

            order.items.add(item)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items")

        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)

        instance.items.all().delete()

        self.context["order"] = instance

        for item_data in items_data:
            item_data["order"] = instance

            item_serializer = ItemSerializer(data=item_data, context=self.context)

            item_serializer.is_valid(raise_exception=True)

            item = item_serializer.save()

            instance.items.add(item)

        instance.save()

        return instance
