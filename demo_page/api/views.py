from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """
    Note: ModelViewSet will handle both the GET and POST for Student without us having to do any more.
    This viewset automatically provides 'list' and 'retrieve'
    """
    queryset = Student.objects.all().order_by("id")
    serializer_class = StudentSerializer