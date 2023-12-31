# Generated by Django 3.2.4 on 2023-10-01 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinicas',
            fields=[
                ('code_clinica', models.IntegerField(auto_created=True, unique=True)),
                ('nit', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nombre_clinica', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('info_contacto', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cpap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=45)),
                ('modelo', models.CharField(max_length=45)),
                ('n_serie', models.CharField(max_length=45)),
                ('config', models.CharField(max_length=45)),
                ('Pacientes_id', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=45, unique=True)),
                ('nombre_pac', models.CharField(max_length=45)),
                ('apellido_pac', models.CharField(max_length=45)),
                ('edad_pac', models.CharField(max_length=45)),
                ('telefono_pac', models.CharField(max_length=45)),
                ('residencia_pac', models.CharField(max_length=45)),
                ('diagnostico_pac', models.CharField(max_length=45)),
                ('Clinica_rut_clinica', models.CharField(max_length=45)),
                ('usuario_id', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presion', models.CharField(max_length=45)),
                ('tiempo_m', models.CharField(max_length=45)),
                ('rampa', models.BooleanField()),
                ('pendiente_rampa', models.CharField(max_length=45)),
                ('tiempo_rampa', models.TimeField()),
                ('porcentaje_humedad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cal_sueno', models.CharField(max_length=45)),
                ('AHI', models.CharField(max_length=45)),
                ('Users_id', models.CharField(max_length=45)),
                ('Cpap_n_serie', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_u', models.IntegerField(auto_created=True, unique=True)),
                ('identificacion', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('contrasena', models.CharField(max_length=45)),
                ('especialidad', models.CharField(max_length=45)),
                ('info_contacto', models.CharField(max_length=25)),
                ('nit_clinica', models.CharField(max_length=45)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
