from django.shortcuts import render
from .models import Flores
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    return render(request,'core/index.html')

@login_required(login_url='/login/')
def galeria(request):
    flor=Flores.objects.all()
    return render(request,'core/galeria.html',{'listaflor':flor})  

@login_required(login_url='/login/')
def quienes_somos(request):
    return render(request,'core/quienes_somos.html')    

@login_required(login_url='/login/')
def formulario(request):
    return render(request,'core/formulario.html')
  
def cerrar_sesion(request):
    return render(request,'core/login')    

@login_required(login_url='/login/')
def eliminar_flor(request,id):
    mensaje=''
    flor=Flores.objects.get(name=id)
    try:
        flor.delete()
        mensaje='Elimino Flor'
    except:
        mensaje='No se pudo eliminar'
    flores=Flores.objects.all()
    return render(request,'core/galeria.html',{'listaflor':flores,'msg':mensaje})

def login(request):
    return render(request,'core/login.html')

def login_iniciar(request):
    msg=''
    if request.POST:
        u=request.POST.get("txtUsuario")
        p=request.POST.get("txtPass")
        usu=authenticate(request,username=u,password=p)
        if usu is not None and usu.is_active:
            auth_login(request,usu)
            return render(request,'core/index.html')
        msg=u
    return render(request,'core/login.html',{'msg':msg})

def cerrar_sesion(request):
    logout(request)
    return HttpResponse("<script>alert('cerro sesion');window.location.href='/';</script>")