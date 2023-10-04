from django.db import models
from django.conf import settings

# Create your models here.


class Users(models.Model):
    id_u = models.IntegerField(auto_created=True, unique=True)
    identificacion = models.CharField(max_length=45,primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
    especialidad = models.CharField(max_length=45)
    info_contacto = models.CharField(max_length=25)
    nit_clinica = models.CharField(max_length=45)
    username = models.OneToOneField(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)

class Clinicas(models.Model):
    code_clinica = models.IntegerField(auto_created=True,unique=True)
    nit = models.CharField(max_length=45,primary_key=True)
    nombre_clinica = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    info_contacto = models.CharField(max_length=45)

class Pacientes(models.Model):
    identificacion=models.CharField(max_length=45,unique=True)
    nombre_pac = models.CharField(max_length=45)
    apellido_pac=models.CharField(max_length=45)
    edad_pac = models.CharField(max_length=45)
    telefono_pac = models.CharField(max_length=45)
    residencia_pac=models.CharField(max_length=45)
    diagnostico_pac=models.CharField(max_length=45)
    Clinica_rut_clinica=models.CharField(max_length=45)
    usuario_id=models.CharField(max_length=45)

class Cpap(models.Model):
    marca=models.CharField(max_length=45)
    modelo=models.CharField(max_length=45)
    n_serie=models.CharField(max_length=45)
    config=models.CharField(max_length=45)
    Pacientes_id=models.CharField(max_length=45)
    
class Registro(models.Model):
    presion=models.CharField(max_length=45)
    tiempo_m=models.CharField(max_length=45)
    rampa=models.BooleanField()
    pendiente_rampa=models.CharField(max_length=45)
    tiempo_rampa=models.TimeField()
    porcentaje_humedad=models.DecimalField(max_digits=5, decimal_places=2)
    cal_sueno=models.CharField(max_length=45)
    AHI=models.CharField(max_length=45)
    Users_id=models.CharField(max_length=45)
    Cpap_n_serie=models.CharField(max_length=45)
