from venv import create

from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Estacionamiento(models.Model):
    nombre = models.CharField(max_length=100)
    dirección = models.TextField(blank=True)
    capacidad_total = models.TextField(blank=True)
    espacios_disponibles = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
