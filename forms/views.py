from django.shortcuts import render, redirect
from django.contrib import messages
from forms.models import Registro, Asistencia, Actividad

def first_form(request):
  if request.method == 'POST':
    identification = request.POST.get('identification')
    user_exists = Registro.objects.filter(numero_documento = identification).exists()

    if user_exists:
      return redirect(attendance_form)
    return redirect(principal_form)
  return render(request, 'first_form.html')

def principal_form(request):
  if request.method == 'POST':
    nombre = request.POST.get('name')
    tipo_documento = request.POST.get('identification_type')
    numero_identificacion = request.POST.get('id_number')
    celular = request.POST.get('phone')
    barrio = request.POST.get('neighborhood')
    grupo_poblacional = request.POST.get('poblational_group')
    genero = request.POST.get('gender_type')

    nuevo_registro = Registro(
            nombre=nombre,
            tipo_documento=tipo_documento,
            numero_documento=numero_identificacion,
            celular=celular,
            Barrio=barrio,
            grupo_poblacional=grupo_poblacional,
            genero=genero
        )
    
    nuevo_registro.save()
    messages.success(request, 'Información almacenada correctamente')
    return redirect(attendance_form)

  return render(request, 'principal_form.html')

def attendance_form(request):
  ultima_actividad = Actividad.objects.latest('fecha')
  if request.method == 'POST':
    nombre = request.POST.get('name')
    numero_identificacion = request.POST.get('id_number')
    celular = request.POST.get('phone')
    organizacion = request.POST.get('organization')
    correo = request.POST.get('email')

    nuevo_registro = Asistencia(
            nombre=nombre,
            numero_documento=numero_identificacion,
            celular=celular,
            organizacion=organizacion,
            correo=correo,
            actividad = ultima_actividad
        )
    
    nuevo_registro.save()
    messages.success(request, 'Información almacenada correctamente')
    return redirect(first_form)
  return render(request, 'attendance_form.html', {'ultima_actividad': ultima_actividad})