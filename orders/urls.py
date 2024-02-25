from django.urls import path

from orders.views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView


orders_patterns = [
    path("", OrderListCreateAPIView.as_view(), name="order-list-create"),
    path(
        "<uuid:pk>/",
        OrderRetrieveUpdateDestroyAPIView.as_view(),
        name="order-retrieve-update-destroy",
    ),
]

urlpatterns = orders_patterns
