from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

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

    def offsprings_count(self,):
        return self.offspring_set.count()

    def __str__(self):
        return f"{self.get_full_name()} <{self.email}>"

    def validate_unique(self, *args, **kwargs):
        super(User, self).validate_unique(*args, **kwargs)
        qs = User.objects.filter(email=self.email)
        if qs.exists():
            raise ValidationError(
                {'email': ['El email no es válido o está repetido', ]})

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    full_name = property(get_full_name)


@receiver(pre_save, sender=User)
def populate_username(sender, instance, *args, **kwargs):
    if instance.email and not instance.username:
        instance.username = instance.email

# Dirección postal
# Nombre apellidos hijos y nombre padres
# Colegio
# Curso
# 3 teléfonos
# 2 mails
# Comentarios

# https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
