from django.contrib import admin
from .models import Users, Clinicas, Pacientes, Cpap, Registro

# Register your models here.

admin.site.register(Users)
admin.site.register(Clinicas)
admin.site.register(Pacientes)
admin.site.register(Cpap)
admin.site.register(Registro)