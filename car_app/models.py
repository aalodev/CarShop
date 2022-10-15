from django.db import models


class Color(models.Model):
    colors = models.CharField(max_length=200)

    def __str__(self):
        return self.colors


class Marka(models.Model):
    marka = models.CharField(max_length=200)

    def __str__(self):
        return self.marka


class Position(models.Model):
    poz = models.CharField(max_length=200)

    def __str__(self):
        return self.poz


class Salon(models.Model):
    brand = models.ForeignKey(Marka, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.price
