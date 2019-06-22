from django.db import models

# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Comediante(models.Model):
    nombre = models.CharField(max_length=20, blank = False)
    apellido = models.CharField(max_length=20, blank = False)
    especialidad = models.CharField(max_length=20, blank = False)
    bio = models.TextField(max_length=200, blank = False)

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)


class Show(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=30, blank = False)
    institucion = models.CharField(max_length=30)
    participantes = models.ManyToManyField(Comediante)

    def __str__(self):
        return self.institucion

    class Meta:
        ordering = ('fecha','hora')
