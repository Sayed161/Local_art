from rest_framework import serializers
from .models import Artists
from Artworks.serializers import Artworks_Serializer

class Artists_Serializer(serializers.ModelSerializer):
    Artworker = Artworks_Serializer(many=True,read_only=True)
    class Meta:
        model = Artists
        fields = '__all__'
