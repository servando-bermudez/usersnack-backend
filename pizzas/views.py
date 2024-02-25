from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from pizzas.models import Extra, Pizza
from pizzas.serializers import PizzaSerializer, ExtraSerializer

from utils.pagination import LimitOffsetPagination


class PizzaListCreateAPIView(ListCreateAPIView):
    """List and create pizzas."""

    queryset = Pizza.objects.all().order_by("name")
    serializer_class = PizzaSerializer
    pagination_class = LimitOffsetPagination


class PizzaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Retrieve, update and destroy a pizza."""

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    allowed_methods = ["GET", "PATCH", "DELETE"]


class ExtraListCreateAPIView(ListCreateAPIView):
    """List and create extras."""

    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer


class ExtraRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Retrieve, update and destroy an extra."""

    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer
    allowed_methods = ["GET", "PATCH", "DELETE"]
