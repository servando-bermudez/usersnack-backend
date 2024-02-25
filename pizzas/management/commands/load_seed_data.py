import json
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from pizzas.models import Extra, Pizza, Ingredient


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Pulling Initial Data from Seed Data..."))

        # Load seed data here
        f = open(BASE_DIR / "seed_data/data.json", "r")
        data = json.load(f)

        self.stdout.write(self.style.SUCCESS("Data Pulled Successfully!"))

        # Create the data here
        self.stdout.write(self.style.SUCCESS("Creating Initial Data..."))

        # Create Extra Objects
        for raw_extra in data.get("extras"):
            _ = Extra.objects.get_or_create(
                name=raw_extra.get("name"), price=raw_extra.get("price")
            )

        # Create Ingredient Objects alongside their respective Pizzas

        for raw_pizza in data.get("pizzas"):
            self.stdout.write(f"Creating Pizza: {raw_pizza.get('name')}...")

            img_file = File(
                open(BASE_DIR / f"seed_data/images/{raw_pizza.get('img')}", "rb")
            )

            pizza = Pizza.objects.create(
                name=raw_pizza.get("name"),
                price=raw_pizza.get("price"),
            )

            pizza.img.save(raw_pizza.get("img"), img_file, save=True)

            pizza.save()

            for raw_ingredient in raw_pizza.get("ingredients"):
                self.stdout.write(
                    f"\tAdding {raw_ingredient} to {raw_pizza.get('name')}..."
                )

                ingredient, _ = Ingredient.objects.get_or_create(
                    name=raw_ingredient,
                )

                pizza.ingredients.add(ingredient)
                pizza.save()

        self.stdout.write(self.style.SUCCESS("Initial Data Created Successfully!"))
