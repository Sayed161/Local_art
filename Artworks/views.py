from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import ArtWorks
from .serializers import Artworks_Serializer

# Create your views here.

class ArtWorks_view(viewsets.ModelViewSet):
    queryset = ArtWorks.objects.all()
    serializer_class = Artworks_Serializer
    permission_classes = [permissions.IsAuthenticated]