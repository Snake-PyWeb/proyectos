from django.shortcuts import render ,redirect # render para mostrar variables que creamos en las vistas y mostrarlas en la templates o archivos html
from django.contrib.auth.forms import UserCreationForm # libreria que incluye django para implementar un formulario de registro 
from django.contrib.auth import login # Libreria que incluye django para incluir autenticacion y verificacion de un usuario cuando se logea
from .models import post # este es el modelo de la base de datos donde se guardan las publicaciones de los post
from .forms import PostForm # esta libreria viene del archivo "forms.py" esta importando el formulario que tiene una clase 
from django.contrib.auth.decorators import login_required

# Create your views here.


""" <<--- Vistas para mostrar archivos htmls --->> """
def index(request): # Vista para mostrar el index
    return render(request,'index.html')

def blogify_view(request):
    posts=post.objects.all() # estamos obteniendo todos los datos de el modelo post que esta en models.py
    return render(request,'blogify.html',{'posts':posts})




def register(request):
    if request.method == 'POST': # verifica si lo que llega del servidor es post , es decir que si el usuario llena el formulario y lo envia pasa al siguinte bloque
        form_register=UserCreationForm(request.POST) # variable que contiene el formulario por defecto de django pero cuando tine requeste.post es por que esta capturando los datos que se escribieron
        if form_register.is_valid():
            user_new=form_register.save() # si el usuario es valido guarda los datos en la base de datos con save 
            login(request,user_new) # cuando el usuario se registre ingresa automaticamente sin necesidad de pedir que inicie sesion
            redirect('blogify')
    else:
        form_register=UserCreationForm() # si no a llenado los datos muestra el formulario 
    return render(request,'register.html',{'form_register':form_register})




@login_required # solo los usuarios logeados pueden crear post
def create_post(request):
    if request.method == 'POST':
        form_create_post=PostForm(request.POST) # variable que contiene el formulario que creamos en el archivo forms.py pero solo esta capturando los datos que se llenan 
        if form_create_post.is_valid():
            post_new=form_create_post.save(commit=False) # todavia no lo guardamos
            post_new.autor=request.user # Asignamos el usuario logueado como autor
            post_new.save() # guardamos el post en la base de datos 
            return redirect('blogify')  
    else:
        form_create_post=PostForm()
    return render(request,'create_post.html',{'form_create_post':form_create_post})


