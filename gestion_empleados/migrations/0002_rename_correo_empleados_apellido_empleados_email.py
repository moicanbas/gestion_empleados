# Generated by Django 4.0.6 on 2022-07-21 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_empleados', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleados',
            old_name='correo',
            new_name='apellido',
        ),
        migrations.AddField(
            model_name='empleados',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
