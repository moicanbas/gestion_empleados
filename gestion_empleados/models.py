from django.db import models

class Empleados(models.Model):
  cedula= models.PositiveBigIntegerField(null=False, blank=False)
  nombre= models.CharField(max_length=100,null=False, blank=False)
  apellido=models.CharField(max_length=100,null=False, blank=False)
  fecha_nacimiento= models.DateField()
  email= models.EmailField()
  celular= models.PositiveBigIntegerField()

  class Meta:
    verbose_name= 'Empleado'
    verbose_name_plural='Empleados'

  def __str__(self):
    return "{0},{1}".format(self.nombre, self.apellido) 
  

