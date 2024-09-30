from django.shortcuts import render,redirect  # Importa la función 'render', que se usa para renderizar plantillas HTML.
from myapp.models import Posts  # Importa el modelo 'Posts' desde el archivo models.py de la aplicación 'myapp'.
from django.contrib.auth.forms import UserCreationForm  # Importa el formulario predeterminado 'UserCreationForm' para el registro de usuarios.
from django.contrib.auth import login  # Importa la función 'login', que se utiliza para autenticar y loguear a un usuario. viene por defecto en django



# Create your views here.

def register(request):
    if request.method =='POST': #  Verifica si la solicitud que llega al servidor es de tipo POST. ,Si la solicitud es de tipo POST, es decir, si el usuario ya envió el formulario, entonces el bloque dentro del if manejará esos datos (es decir, procesará la información enviada).
        form=UserCreationForm(request.POST) # con request.POST como argumento, le estás diciendo a Django que llene el formulario con los datos enviados por el usuario.
        if form.is_valid(): # Verificamos que el formulario sea valido que cuando llene cada campo este bien escrito y con las reglas , is_valid() viene por defecto en django para verificar que todos los campos del formulario esten llenos , verifca por ejeplo el formato de los correos electronicos 
            user=form.save() # Si el formulario es válido, este código guarda el usuario en la base de datos. 
            login(request,user) # La función login() de Django autentica al usuario y establece una sesión. Después de que se crea el usuario con form.save(), esta función hace que el usuario recién registrado inicie sesión automáticamente, 
            return redirect('post_list')  # Redirige a la lista de posts
    else:
        form=UserCreationForm() #Si no incluyes request.POST, estarías creando un formulario vacío, que normalmente se utiliza cuando se muestra el formulario por primera vez, antes de que el usuario lo envíe.
    return render(request,'register.html',{'form':form}) #envia los datos por medio de la funcion render al archivo html que esta en templates


def post_list(request):
    posts=Posts.objects.all() #Recupera todos los posts de la base de datos 
    return render(request,'post_list.html' ,{'posts':posts}) # Pasa los posts al template
    


# vista para crear publicaciones 

