# Generated by Django 4.2.10 on 2024-02-25 12:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Extra",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Ingredient Name"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Price"
                    ),
                ),
            ],
            options={
                "verbose_name": "Extra",
                "verbose_name_plural": "Extras",
            },
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Ingredient Name"
                    ),
                ),
            ],
            options={
                "verbose_name": "Ingredient",
                "verbose_name_plural": "Ingredients",
            },
        ),
        migrations.CreateModel(
            name="Pizza",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "img",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/pizzas/"
                    ),
                ),
                (
                    "ingredients",
                    models.ManyToManyField(
                        related_name="pizzas", to="pizzas.ingredient"
                    ),
                ),
            ],
        ),
    ]
