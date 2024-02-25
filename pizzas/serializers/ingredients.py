from rest_framework import serializers

from pizzas.models import Extra, Ingredient


# The `IngredientSerializer` class in Python handles serialization, validation, and creation of
# Ingredient objects.
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

    def validate(self, attrs):
        if self.instance:
            if self.instance.pizzas.exists():
                raise serializers.ValidationError(
                    "You can't update an ingredient that is already in use."
                )
        return attrs

    def create(self, validated_data):
        ingredient, _ = Ingredient.objects.get_or_create(**validated_data)
        return ingredient


# This class is a Django REST framework serializer for the Extra model with a custom create method
# that either creates a new instance or retrieves an existing one based on the validated data.
class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = "__all__"

    def create(self, validated_data):
        extra, _ = Extra.objects.get_or_create(**validated_data)
        return extra
