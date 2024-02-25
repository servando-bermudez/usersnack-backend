from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from orders.models import Order
from orders.serializers import OrderSerializer

from utils.pagination import LimitOffsetPagination


# This class is a Django REST framework API view for listing and creating Order objects.
class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderSerializer
    pagination_class = LimitOffsetPagination


# This class is a Django REST framework API view for retrieving, updating, and deleting Order objects.
class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
