# Generated by Django 4.0.6 on 2022-07-20 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.PositiveBigIntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.CharField(max_length=100)),
                ('celular', models.PositiveBigIntegerField()),
            ],
        ),
    ]
