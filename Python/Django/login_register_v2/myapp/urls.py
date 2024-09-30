from django .urls import path
from django.contrib.auth import views as auth_viws # Esto libreria vine por defecto en django para crear un formulario de login vine con campos basicos
from .views import register,post_list 


urlpatterns=[
    path('login/',auth_viws.LoginView.as_view(template_name='login.html'),name='login'), #Estás usando la vista genérica de login que Django provee por defecto: LoginView. Esta vista ya incluye el formulario de inicio de sesión, por lo que no necesitas crearlo manualmente.
    path('',post_list,name='post_list'),
    path('register/',register,name='register')
]

""" Resumen:
No ves el formulario de login explícitamente porque LoginView de Django ya lo gestiona.
AuthenticationForm es el formulario que se utiliza internamente por esta vista genérica de Django.
Solo necesitas asegurarte de tener la plantilla login.html y la ruta a LoginView en tu archivo de URLs. """

#auth_views.LoginView: Es una vista basada en clase que maneja el formulario de inicio de sesión. auth_viws solo es un alias que le dimos a la funcion views que importamos arriba 

#.as_view(): Este método convierte la clase LoginView en una función de vista que puede recibir una solicitud (request), procesarla y devolver una respuesta.

