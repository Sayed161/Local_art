from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,permissions
from .models import Artists
from .serializers import Artists_Serializer

# Create your views here.

class Artists_View(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = Artists_Serializer
    permission_classes = [permissions.IsAuthenticated]
