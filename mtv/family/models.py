from unicodedata import name
from django.db import models


class Family_member(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    relationship = models.CharField(max_length=40) 

    def __str__(self):
        return f'Nombre: {self.name} | Apellido: {self.last_name} | Edad: {self.age} | Relación: {self.relationship} '
