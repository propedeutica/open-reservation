# Generated by Django 3.0.8 on 2020-07-10 16:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offspring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=75, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=150, verbose_name='apellidos')),
                ('grade', models.IntegerField(choices=[(1, 'Primero de Primaria'), (2, 'Segundo de Primaria'), (3, 'Tercero de Primaria'), (0, 'Otros')], default=1, verbose_name='curso')),
                ('birth_date', models.DateField(default=datetime.date.today, verbose_name='fecha de nacimiento')),
                ('school', models.CharField(default='Nombre del colegio', max_length=150, verbose_name='colegio')),
                ('home_address', models.CharField(default='Dirección completa de la casa del catecúmeno', max_length=150, verbose_name='dirección')),
                ('baptized', models.BooleanField(default=True, verbose_name='bautizado')),
                ('father_name', models.CharField(default='nombre completo del padre', max_length=150, verbose_name='nombre completo del padre')),
                ('mother_name', models.CharField(default='nombre completo de la madre', max_length=150, verbose_name='nombre completo de la madre')),
                ('assignment', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedules.Schedule', verbose_name='turno')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='padre o tutor')),
            ],
        ),
    ]
