from django import forms
from .models import Empleados

class empleado_form(forms.ModelForm):

  class Meta:
    model= Empleados
    fields= ['cedula','nombre','apellido','fecha_nacimiento','email','celular']
    