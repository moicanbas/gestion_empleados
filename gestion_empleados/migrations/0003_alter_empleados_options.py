# Generated by Django 4.0.6 on 2022-07-21 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_empleados', '0002_rename_correo_empleados_apellido_empleados_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleados',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]
