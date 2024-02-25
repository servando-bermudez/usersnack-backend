from rest_framework import pagination


# The class `LimitOffsetPagination` sets default and maximum limits for pagination in Python.
class LimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 20
    max_limit = 100
