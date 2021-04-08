from django.urls import path,  include
from rest_framework import routers
from . import views

"""
The REST Framework router will make sure our requests end up at the right resource dynamically.
"""

# create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# the API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]