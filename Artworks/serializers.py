from rest_framework import serializers
from .models import ArtWorks

class Artworks_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWorks
        fields = '__all__'