from rest_framework import serializers
from . import models


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = '__all__'


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marka
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = '__all__'


class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Salon
        fields = '__all__'
