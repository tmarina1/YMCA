from django.db import models

# Create your models here.
class Registro(models.Model):
  nombre = models.CharField(max_length=255)
  tipo_documento = models.CharField(max_length=20)
  numero_documento = models.CharField(max_length=30)
  celular = models.CharField(max_length=30)
  Barrio = models.CharField(max_length=255)
  grupo_poblacional = models.CharField(max_length=255)
  genero = models.CharField(max_length=10)

class Actividad(models.Model):
  objetivo = models.CharField(max_length=255)
  nombre = models.CharField(max_length=255)
  profesional = models.CharField(max_length=255)
  lugar = models.CharField(max_length=255)
  fecha = models.DateTimeField(null=True)

class Asistencia(models.Model):
  nombre = models.CharField(max_length=255)
  numero_documento = models.CharField(max_length=30)
  celular = models.CharField(max_length=30)
  organizacion = models.CharField(max_length=255)
  correo = models.CharField(max_length=255)
  actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name="asistencias", null=True, blank=True)

