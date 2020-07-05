from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(AbstractUser):
    phone = PhoneNumberField(null=False, blank=False, verbose_name="teléfono")
    phone2 = PhoneNumberField(null=True, blank=True, verbose_name="teléfono 2 (opcional)")
    phone3 = PhoneNumberField(null=True, blank=True, verbose_name="teléfono 3 (opcional)")
    offsprings_surname = models.CharField(
        "apellidos de los catecúmenos",
        null=True,
        blank=False,
        max_length=150,
        )
    father_name = models.CharField(
        "nombre completo del padre", 
        max_length=150, 
        default="nombre del padre",
        )
    mother_name = models.CharField(
        "nombre completo de la madre", 
        max_length=150, 
        default="nombre de la madre",
        )
    
    comments = models.TextField(
        "comentarios",
        max_length=500,
        blank=True,
        )



    #Dirección postal
    # Nombre apellidos hijos y nombre padres
    #Colegio 
    #Curso
    #3 teléfonos 
    #2 mails
    # Comentarios


# https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models