from django.urls import path
from .views import UsersView, ClinicasView, PacientesView,CpapView,RegistroView, cpaps, CatchUser, users, exit

urlpatterns=[
    path('users/', UsersView.as_view(), name='users_list'),
    path('users/<int:id>' , UsersView.as_view() , name='usuarios_process'),
    path('clinicas/', ClinicasView.as_view(), name='users_list'),
    path('clinicas/<int:rut_clinicas>' , ClinicasView.as_view() , name='usuarios_process'),
    path('pacientes/',PacientesView.as_view(),name='users_list'),
    path('pacientes/<int:id>',PacientesView.as_view(),name='usuarios_process'),
    path('cpaps/',CpapView.as_view(),name='users_list'),
    path('cpaps/<int:n_serie>' , CpapView.as_view() , name='usuarios_process'),
    path('registros/', RegistroView.as_view(), name='users_list'),
    path('registros/<int:id>' , RegistroView.as_view() , name='usuarios_process'),
    path('registrof', cpaps, name='cpaps'),
    path('user_data/<int:us_id>', CatchUser.as_view(), name='catch_user'),
    path('usuarioactual', users, name = 'users'),
    path('logout/', exit, name='exit')
]