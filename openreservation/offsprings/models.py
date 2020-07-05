from django.db import models
from parents.models import User
from schedules.models import Schedule
import datetime


class Offspring(models.Model):
    GRADES = [
        (1, "Primero de Primaria"),
        (2, "Segundo de Primaria"),
        (3, "Tercero de Primaria"),
        (0, "Otros"),
    ]

    first_name = models.CharField("nombre", max_length=75)
    last_name = models.CharField("apellidos", max_length=150)
    grade = models.IntegerField("curso", choices=GRADES, default=1)
    parent = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="padre o tutor")

    assignment = models.ForeignKey(
        Schedule, on_delete=models.SET_NULL, verbose_name="turno", null=True, default=None)

    birth_date = models.DateField(
        "fecha de nacimiento", default=datetime.date.today)
    school = models.CharField("colegio", max_length=150, default="Nombre del colegio")
    home_address = models.CharField(
        "dirección", max_length=150, default="Dirección completa de la casa del catecúmeno")
    baptized = models.BooleanField("bautizado", default=True)
    father_name = models.CharField(
        "nombre completo del padre", max_length=150, default="nombre completo del padre")
    mother_name = models.CharField(
        "nombre completo de la madre", max_length=150, default="nombre completo de la madre")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.last_name = self.parent.offsprings_surname
        self.father_name = self.parent.father_name
        self.mother_name = self.parent.mother_name
        super().save(*args, **kwargs)
