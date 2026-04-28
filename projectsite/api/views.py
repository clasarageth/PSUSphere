from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from studentorg.models import College
from .serializers import CollegeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# List all or create new colleges (protected)
class CollegeListCreateAPIView(generics.ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]  # Require login or token

# Retrieve, update, or delete a single college (protected)
class CollegeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]  # Require login or token