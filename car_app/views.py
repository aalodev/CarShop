from django.shortcuts import render
from rest_framework import generics
from . import models, serializers


class ListColor(generics.ListCreateAPIView):
    serializer_class = serializers.ColorSerializer
    queryset = models.Color.objects.all()


class DetailColor(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ColorSerializer
    queryset = models.Color.objects.all()


class ListMarka(generics.ListCreateAPIView):
    serializer_class = serializers.MarkaSerializer
    queryset = models.Marka.objects.all()


class DetailMarka(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MarkaSerializer
    queryset = models.Marka.objects.all()


class ListPosition(generics.ListCreateAPIView):
    serializer_class = serializers.PositionSerializer
    queryset = models.Position.objects.all()


class DetailPosition(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PositionSerializer
    queryset = models.Position.objects.all()


class ListSalon(generics.ListCreateAPIView):
    serializer_class = serializers.SalonSerializer
    queryset = models.Salon.objects.all()


class DetailSalon(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.SalonSerializer
    queryset = models.Salon.objects.all()
