"""
- we need to render the different heroes in JSON format
- To do this we need to:
1. Query the database for all heroes
2. Pass that databases queryset into the serializer we just created, so that it gets converted into JSON and rendered.
"""
from django.shortcuts import render
from .models import Hero
from .serializers import HeroSerializer
from rest_framework import viewsets # provides operations such as retrieve and update
# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    """
    Note: ModelViewSet will handle GET and POST for Heroes without us having to do any more work.
    This viewset automatically provides 'list' and 'retrieve' actions
    """
    queryset = Hero.objects.all().order_by("id")
    serializer_class = HeroSerializer
    