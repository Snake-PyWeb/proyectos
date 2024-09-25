from django.shortcuts import render, redirect # la libreria redirect nos sirve para redirigir a una pagina si se cumple una condicion 
import json, os # importamos estas librerias para poder usar y cargar el archivo json donde contiene los usuarios

# Obtener la ruta base de tu proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ruta al archivo JSON, asumiendo que está en una carpeta 'data' en la raíz del proyecto
json_path = os.path.join(BASE_DIR, 'data', 'usuarios.json')

def index(request): # funcion para redirigir los enlaces a la pagina principal o home
    return render(request, "index.html")


def admin_panel(request): # funcion para redirigir los enlaces al formulario de inicio
    return render(request, 'admin_panel.html')



def login(request):
    # Utiliza la ruta absoluta definida en json_path
    with open(json_path, 'r') as archivo_json:
        usuarios = json.load(archivo_json)

    mensaje_error = None # se tiene que establecer en None para que podamos usar el mensaje en el mismo formulario 

    nombre_usuario = request.POST.get('nombre_usuario') 
    contra_usuario = request.POST.get('contra_usuario')

    if nombre_usuario and contra_usuario: # si estan vacias aparece el error " por favor ingrese las credenciales "
        for nombre, datos in usuarios.items(): # recorre el diccionario buscando concidencias , si concide cumple y lo lleva al panel 
            if datos["nombre_usuario"] == nombre_usuario and datos["contra_usuario"] == contra_usuario:
                # Si las credenciales coinciden, redirigir al panel de administrador
                return redirect('admin_panel') # redirigir al panel del administrador si cumple 
        mensaje_error = 'NOMBRE DE USUARIO O CONTRASEÑA INCORRECTA' # si la contraseña o el usuario no conciden aparece este error
    else:
        mensaje_error = 'Por favor ingrese sus credenciales.' # si los campos del formulario estan vacios aparece este error

    return render(request, "login.html", {'Error': mensaje_error}) # si retornamos de esta manera no es necesario crear un url para el formulario , tambien  nos sirve para mostrar mensajes en el html 





def register(request): # Funcion que va registrar a los nuevos usuarios
    with open(json_path, 'r') as archivo_json:
        usuarios = json.load(archivo_json)

    mensaje_error = None

    if request.method == "POST":
        nombre_usuario = request.POST.get("nombre_usuario")
        contra_usuario = request.POST.get("contra_usuario")
        tel_recuperacion = request.POST.get("tel_recuperacion")

        # Verificación simple para evitar campos vacíos
        if not nombre_usuario or not contra_usuario or not tel_recuperacion:
            mensaje_error = 'Por favor complete todos los campos.'
        else:
            nuevo_usuario = {
                'nombre_usuario': nombre_usuario,
                'contra_usuario': contra_usuario,
                'tel_recuperacion': tel_recuperacion
            }

            nuevo_nombre_usuario = f'user{len(usuarios) + 1}' # Crea un nuevo nombre de usuario en el formato 'user#', donde # es el número total de usuarios + 1

            usuarios[nuevo_nombre_usuario] = nuevo_usuario # Agrega el nuevo usuario al diccionario de usuarios con el nuevo nombre de usuario como clave

            with open(json_path, 'w') as archivo_json:
                json.dump(usuarios, archivo_json, indent=4)

            return redirect('login')  # Redirigir a la página de login después de registrarse

    # Si no es una solicitud POST o hay un error, renderiza el formulario de registro con el mensaje de error
    return render(request, "register.html", {'Error': mensaje_error})  #'Error' es el nombre que tenemos que poner en el html para que aparezca

