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

@login_required(login_url='/login/')
def agregar_carro(request, id):
    flor=Flores.objects.filter(name__contains=id)
    precio=Flores.precio
    sesion=request.session.get("carro","")
    arr=sesion.split(";")
    arr2=''
    sw=0
    cant=1
    for f in arr:
        flo=f.split(":")        
        if flo[0]==id:
            cant=int(flo[1])+1
            sw=1
            arr2=arr2+str(flo[0])+":"+str(cant)+":"+str(precio)+";"            
        elif not flo[0]=="":
            cant=flo[1]
            arr2=arr2+str(flo[0])+":"+str(cant)+":"+str(precio)+";"

    if sw==0:
        arr2=arr2+str(id)+":"+str(1)+":"+str(precio)+";"
    request.session["carro"]=arr2
    flores=Flores.objects.all()
    msg='Agrego Flor'
    return render(request,'core/galeria.html',{'listflores':flores,'msg':msg})

@login_required(login_url='/login/')
def carrito(request):
    lista=request.session.get("carro","")
    arr=lista.split(";")
    return render(request,"core/carrito.html",{'lista':arr})

def vacio_carrito(request):
    request.session["carro"]=""
    lista=request.session.get("carro","")
    return render(request,"core/carrito.html",{'lista':lista})
