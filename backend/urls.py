"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
)


# The `admin_patterns` variable is defining a list of URL patterns for the Django admin interface.
# In this case, it includes a single URL pattern that maps requests to the "/admin/" endpoint to the Django admin site.

# This means that when a user navigates to the "/admin/" URL of the backend project,
# they will be directed to the Django admin interface where they can manage the site's data and configurations.
admin_patterns = [
    path("admin/", admin.site.urls),
]


# The `documentation_patterns` variable is defining a list of URL patterns for handling documentation
# related endpoints in a Django project.

documentation_patterns = [
    path("documentation/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "documentation/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]


# These code snippets are defining URL patterns for different parts of an API in a Django project.
pizza_patterns = [
    path("pizzas/", include("pizzas.urls")),
]

orders_patterns = [
    path("orders/", include("orders.urls")),
]

media_patterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# The line `urlpatterns = admin_patterns + documentation_patterns + pizza_patterns + orders_patterns`
# in the Django URL configuration file is combining different sets of URL patterns into a single list
# called `urlpatterns`.
urlpatterns = (
    admin_patterns
    + documentation_patterns
    + pizza_patterns
    + orders_patterns
    + media_patterns
)
