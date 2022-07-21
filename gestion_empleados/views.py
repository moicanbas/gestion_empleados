from django.shortcuts import redirect, render
from .models import Empleados
from .forms import empleado_form

def home(request):
  empleado= Empleados.objects.all()
  context={'empleado':empleado}
  return render(request,'./home.html', context)

def agregar(request):
  if request.method == 'POST':
    form = empleado_form(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  
  else:
    form= empleado_form()

  context={'form': form}
  return render(request,'./agregar.html',context)

def eliminar(request, empleado_id):
 empleado= Empleados.objects.get(id=empleado_id)
 empleado.delete()
 return redirect('home')

def editar(request, empleado_id):
  empleado= Empleados.objects.get(id=empleado_id)
  if request.method== "POST":
    form = empleado_form(request.POST, instance=empleado)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form =empleado_form(instance=empleado)

  context={'form': form}
  return render(request,'./editar.html',context)
  