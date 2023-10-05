from django.views import View
from .models import Users, Clinicas, Pacientes, Cpap, Registro
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'view/home.html')

@login_required
def cpaps(request):
    return render(request, 'view/cpaps.html')

def login(request):
    return render(request, 'register/login.html')

class UsersView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, id_u=0):
        if (id_u>0):
            users = list(Users.objects.filter(id_u=id_u).values())
            if len(users)>0:
                user = users[0]
                data = {"message" : "Sucess" , "users" : users}
                #print(data)
            else:
                data = {"message":"No user with this ID"}
            return JsonResponse(data)
        else:
            users = list(Users.objects.values())

            if len(users)>0:
                data = {"message" : "Sucess" , "users" : users}
            else:
                data = {"message":"No user with this ID"}

            return JsonResponse(data)

    def post(self,request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Users.objects.create(nombre=jd['name'], apellido=jd['lastname'] , identificacion=jd['id_u'], especialidad=jd['speciality'], contrasena=jd['password'],info_contacto=jd['contact'],nit_clinica=jd['nit'])
        data = {"message":"Success"}
        return JsonResponse(data)

    def put(self,request,id_u):
        jd = json.loads(request.body)
        users = list(Users.objects.filter(id_u=id_u).values())
        if len(users)>0:
            user = Users.objects.get(id_u=id_u)
            user.nombre=jd['name']
            user.apellido=jd['lastname']
            user.especialidad=jd['speciality']
            user.contrasena=jd['passord']
            user.info_contacto=jd['contact']
            user.nit_clinica=jd['nit']
            user.save()
            data = {"message":"Success"}
        else:
            data = {"message":"No user with this ID"}
        return JsonResponse(data)

    def delete(self,request,id_u):
        users = list(Users.objects.filter(id_u=id_u).values())
        if len(users)>0:
            Users.objects.filter(id_u=id_u).delete()
            data = {"message":"Sucess"}
        else:
            data = {"message":"No user with this ID"}
        return JsonResponse(data)
    
class ClinicsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, code_clinica=0):
        if (code_clinica>0):
            clinicas = list(Clinicas.objects.filter(code_clinica=code_clinica).values())
            if len(clinicas)>0:
                clinica = clinicas[0]
                data = {"message" : "Success" , "clinics" : clinicas}
                #print(data)
            else:
                data = {"message":"No clinic with such code"}
            return JsonResponse(data)
        else:
            clinicas = list(Clinicas.objects.values())

            if len(clinicas)>0:
                data = {"message" : "Success" , "clinics" : clinicas}
            else:
                data = {"message":"No clinic with such code"}
            return JsonResponse(data)

    def post(self,request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Clinicas.objects.create(nit=jd['nit'], nombre_clinica=jd['name'] , direccion=jd['address'], info_contacto=jd['contact'])
        data = {"message":"Success"}
        return JsonResponse(data)

    def put(self,request,code_clinica):
        jd = json.loads(request.body)
        clinicas = list(Clinicas.objects.filter(code_clinica=code_clinica).values())
        if len(clinicas)>0:
            clinica = Clinicas.objects.get(code_clinica=code_clinica)
            clinica.nombre_clinica=jd['name'] 
            clinica.direccion=jd['address']
            clinica.info_contacto=jd['contact']
            clinica.save()
            data = {"message":"Success"}
        else:
            data = {"message":"No clinic with such code"}
        return JsonResponse(data)

    def delete(self,request,code_clinica):
        clinicas = list(Clinicas.objects.filter(code_clinica=code_clinica).values())
        if len(clinicas)>0:
            Clinicas.objects.filter(code_clinica=code_clinica).delete()
            data = {"message":"Success"}
        else:
            data = {"message":"No clinic with such code"}
        return JsonResponse(data)
    
class CatchUser(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,us_id = 0):
        users = list(Users.objects.filter(username_id = us_id).values())
        if len(users)>0:
            data = {"message" : "Sucess" , "users" : users}
        else:
            data = {"message":"No hay un usuario logeado"}
 
        return JsonResponse(data)

@login_required
def users(request):
    us_id = request.user.id
    if us_id is None:
        print(us_id)
        print(us_id)
        print(us_id)
        print(us_id)
        response = requests.get('http://127.0.0.1:8000/api/user_data/'+'9999999999999999999999999999999999999')
        users = response.json()
        print(users)
        return render(request, "users.html", {'users': users})
    else:
        #pull data from third party rest api
        response = requests.get('http://127.0.0.1:8000/api/user_data/'+str(us_id))
        #convert reponse data into json
        users = response.json()
        return render(request, "users.html", {'users': users['users'][0]})
    
def exit(request):
    logout(request)
    return redirect('users')
    

class PacientesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, id=0):
        if (id>0):
            pacientes = list(Pacientes.objects.filter(id=id).values())
            if len(pacientes)>0:
                user = pacientes[0]
                data = {"message" : "Completado con éxito" , "pacientes" : pacientes}
                #print(data)
            else:
                data = {"message":"No existe un paciente con dicha id"}
            return JsonResponse(data)
        else:
            pacientes = list(Pacientes.objects.values())

            if len(pacientes)>0:
                data = {"message" : "Completado con éxito" , "pacientes" : pacientes}
            else:
                data = {"message":"No existe un paciente con dicha id"}
            return JsonResponse(data)
    def put(self,request,id):
        jd = json.loads(request.body)
        pacientes = list(Pacientes.objects.filter(id=id).values())
        if len(pacientes)>0:
            paciente = Pacientes.objects.get(id=id)
            paciente.identificacion=jd['identificacion']
            paciente.nombre_pac=jd['nombre'] 
            paciente.apellido_pac=jd['apellido']
            paciente.edad_pac=jd['contacto']
            paciente.telefono_pac=jd['telefono']
            paciente.residencia_pac=jd['residencia']
            paciente.diagnostico_pac=jd['diagnostico']
            paciente.rut_clinica=jd['rut_clinica']
            paciente.usuario_id=jd['usuario_id']
            paciente.save()
            data = {"message":"Completado con éxito"}
        else:
            data = {"message":"No existe un paciente con dicha id"}
        return JsonResponse(data)
    
    def delete(self,request,id):
        pacientes = list(Pacientes.objects.filter(id=id).values())
        if len(pacientes)>0:
            Pacientes.objects.filter(id=id).delete()
            data = {"message":"Completado con éxito"}
        else:
            data = {"message":"No existe un paciente con dicha id"}
        return JsonResponse(data)
    
    def post(self,request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Pacientes.objects.create(nombre_pac=jd['nombre'] ,identificaion=jd['identificacion'], apellido_pac=jd['apellido'], edad_pac=jd['edad'],telefono_pac=jd['telefono'],residencia_pac=jd['residencia'],diagnostico_pac=jd['diagnostico'],rut_clinica=jd['rut_clinica'],usuario_id=jd['usuario_id'] )
        data = {"message":"Completado con éxito"}
        return JsonResponse(data)
    
class CpapView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, n_serie=0):
        if (n_serie>0):
            cpaps = list(Cpap.objects.filter(n_serie=n_serie).values())
            if len(cpaps)>0:
                cpap = cpaps[0]
                data = {"message" : "Completado con éxito" , "CPAP" : cpaps}
                #print(data)
            else:
                data = {"message":"No existe un CPAP con dicho numero de serie"}
            return JsonResponse(data)
        else:
            cpaps = list(Cpap.objects.values())

            if len(cpaps)>0:
                data = {"message" : "Completado con éxito" , "CPAP" : cpaps}
            else:
                data = {"message":"No existe un CPAP con dicha NUmero de serie"}
            return JsonResponse(data)

    def post(self,request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Users.objects.create(marca=jd['marca'], modelo=jd['modelo'] , n_serie=jd['numero de serie'], config=jd['config'], Pacientes_id=jd['Pacieentes_id'])
        data = {"message":"Completado con éxito"}
        return JsonResponse(data)

    def put(self,request,n_serie):
        jd = json.loads(request.body)
        cpaps = list(Cpap.objects.filter(id=n_serie).values())
        if len(cpaps)>0:
            cpap = Cpap.objects.get(id=n_serie)
            cpap.marca=jd['marca']
            cpap.modelo=jd['modelo']
            cpap.config=jd['config']
            cpap.n_serie=jd['numero de serie']
            cpap.Pacientes_id=jd['Paciente_id']
            cpap.save()
            data = {"message":"Completado con éxito"}
        else:
            data = {"message":"No existe un CPAP con dicha id"}
        return JsonResponse(data)

    def delete(self,request,n_serie):
        cpaps = list(Cpap.objects.filter(n_serie=n_serie).values())
        if len(cpaps)>0:
            Cpap.objects.filter(id=id).delete()
            data = {"message":"Completado con éxito"}
        else:
            data = {"message":"No existe un CPAP con dicha numero de serie"}
        return JsonResponse(data)

class RegistroView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, id=0):
        if (id>0):
            registros = list(Registro.objects.filter(id=id).values())
            if len(registros)>0:
                registro = registros[0]
                data = {"message" : "Completado con éxito" , "registrosss" : registros}
                #print(data)
            else:
                data = {"message":"No existe un Registro con dicha id"}
            return JsonResponse(data)
        else:
            registros = list(Registro.objects.values())

            if len(registros)>0:
                data = {"message" : "Completado con éxito" , "registross" : registros}
            else:
                data = {"message":"No existe un registro con dicha id"}
            return JsonResponse(data)

    def post(self,request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Registro.objects.create(presion=jd['presion'], tiempo_m=jd['tiempo_m'] , id=jd['id_u'], rampa=jd['rampa'], pendiente_rampa=jd['pedniente_rampa'],tiempo_rampa=jd['tiempo rampa'],porcentaje_humedad=jd['porcentaje de humedad'],cal_sueno=jd['calidad sueño'],AHI=jd['AHI'],Users_id=jd['Usuario id'],Cpap_n_serie=jd['Numero de serie del Cpap'])
        data = {"message":"Completado con éxito"}
        return JsonResponse(data)

    def put(self,request,id):
        jd = json.loads(request.body)
        registros = list(Registro.objects.filter(id=id).values())
        if len(registros)>0:
            registro = Registro.objects.get(id=id)
            registro.presion=jd['presion']
            registro.tiempo_m=jd['tiempo m']
            registro.rampa=jd['rampa']
            registro.pendiente_rampa=jd['pendiente_rampa']
            registro.tiempo_rampa=jd['Tiempo rampa']
            registro.porcentaje_humedad=jd['Parcentaje de humedad']
            registro.cal_sueno=jd['calidad de sueño']
            registro.AHI=jd['AHI']
            registro.Users_id=jd['Id del usuario']
            registro.Cpap_n_serie=jd['Numero de serie del cpap']
            registro.save()
            data = {"message":"Completado con éxito"}
        else:
            data = {"message":"No existe un REGISTRO con dicha id"}
        return JsonResponse(data)

    def delete(self,request,id):
        registros = list(Registro.objects.filter(id=id).values())
        if len(registros)>0:
            Registro.objects.filter(id=id).delete()
            data = {"message":"Completado con éxito"}
        else:
            data = {"message":"No existe un REGISTRO con dicha id"}
        return JsonResponse(data)
