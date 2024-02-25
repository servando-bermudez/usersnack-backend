from rest_framework import serializers

from orders.models import Item, Order
from pizzas.models import Extra, Pizza
from pizzas.serializers import ExtraSerializer, PizzaSerializer


class ItemSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer(read_only=True)
    pizza_id = serializers.CharField(write_only=True)

    extras = ExtraSerializer(many=True, read_only=True)
    extras_id = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        allow_empty=True,
        required=False,
    )

    total = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)

    class Meta:
        model = Item
        fields = (
            "id",
            "quantity",
            # write-only fields
            "extras_id",
            "pizza_id",
            # Read-only fields
            "extras",
            "pizza",
            "total",
        )
        read_only_fields = ("total",)

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        pizza_id = validated_data.get("pizza_id")
        extras_id = validated_data.get("extras_id", [])

        try:
            pizza = Pizza.objects.get(id=pizza_id)
            validated_data["pizza"] = pizza
        except Pizza.DoesNotExist:
            raise serializers.ValidationError("Pizza does not exist")

        extras = []
        for extra_id in extras_id:
            try:
                extra = Extra.objects.get(id=extra_id)
                extras.append(extra)
            except Extra.DoesNotExist:
                raise serializers.ValidationError("Extra does not exist")

        validated_data["extras"] = extras

        return validated_data

    def create(self, validated_data):
        validated_data["order"] = self.context.get("order", None)

        validated_data.pop("extras_id")
        extras = validated_data.pop("extras")

        item = Item.objects.create(**validated_data)

        for extra in extras:
            item.extras.add(extra.id)

        return item
