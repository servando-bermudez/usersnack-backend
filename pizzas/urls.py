from django.urls import path

from .views import (
    ExtraListCreateAPIView,
    ExtraRetrieveUpdateDestroyAPIView,
    PizzaListCreateAPIView,
    PizzaRetrieveUpdateDestroyAPIView,
)


ingredients_patterns = []

extras_patterns = [
    path("extras/", ExtraListCreateAPIView.as_view(), name="list-create-extras"),
    path(
        "extras/<uuid:pk>/",
        ExtraRetrieveUpdateDestroyAPIView.as_view(),
        name="retrieve-update-destroy-extra",
    ),
]

pizzas_patterns = [
    path("", PizzaListCreateAPIView.as_view(), name="list-create-pizzas"),
    path(
        "<uuid:pk>/",
        PizzaRetrieveUpdateDestroyAPIView.as_view(),
        name="retrieve-update-destroy-pizza",
    ),
]

urlpatterns = pizzas_patterns + extras_patterns + ingredients_patterns
