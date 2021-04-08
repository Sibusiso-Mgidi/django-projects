from django.urls import path, include
from rest_framework import routers
from . import views

# create a router and register our viewsets with it
router = routers.DefaultRouter()
router.register(r"students", views.StudentViewSet)

# the API URLs are now determined automatically by the router
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/",   include("rest_framework.urls", namespace="rest_framework"))
]