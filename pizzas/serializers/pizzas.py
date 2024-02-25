from rest_framework import serializers

from pizzas.models import Pizza
from pizzas.serializers.ingredients import IngredientSerializer


# The `PizzaSerializer` class serializes and deserializes Pizza objects with nested Ingredient
# objects.
class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Pizza
        fields = "__all__"

    def create(self, validated_data):
        ingredients_data = validated_data.pop("ingredients")
        pizza = Pizza.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient_serializer = IngredientSerializer(data=ingredient_data)
            ingredient_serializer.is_valid(raise_exception=True)
            ingredient = ingredient_serializer.create(ingredient_data)
            pizza.ingredients.add(ingredient)
        return pizza
