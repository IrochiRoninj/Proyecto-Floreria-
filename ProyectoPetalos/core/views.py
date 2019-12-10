from django.shortcuts import render
from .models import Flores
from .models import Opinion
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
    return render(request,'core/galeria.html',{'lista':flor})  

@login_required(login_url='/login/')
def quienes_somos(request):
    return render(request,'core/quienes_somos.html')    

@login_required(login_url='/login/')
def formulario2(request):
    
    if request.POST:
        nomflor=request.POST.get("txtNombreFlor")
        precio=request.POST.get("txtPrecio")
        descripcion=request.POST.get("txtDescripcion")
        esta=request.POST.get("txtEstado")
        sto=request.POST.get("txtStock")
        if esta=='on':
            es=True
        else:
            es=False
        imagen=request.FILES.get("txtImagen")
        flor=Flores(
            name=nomflor,
            precio=precio,
            descripcion=descripcion,
            estado=es,
            imagen=imagen,
            stock=sto
        )
        flor.save()
        flores=Flores.objects.all() 
        return render(request,'core/formulario2.html',{'lista':flores,'msg':'grabo','sw':True})
    flores=Flores.objects.all()
    return render(request,'core/formulario2.html',{'lista':flores})

@login_required(login_url='/login/')
def formulario (request):
    mensaje=''
    sw=False
    if request.POST:
        accion=request.POST.get("Accion")
        if accion=="Enviar":
            name=request.POST.get("txtNomFlor")
            opi=request.POST.get("txtOpinion")
            OPI=Opinion(
                name=name,
                opinion=opi
            )
            OPI.save()
            mensaje='Enviado'    
            sw=True
    opinion=Opinion.objects.all()
    return render(request,'core/formulario.html',{'lista':opinion,'msg':mensaje,'sw':True})

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
    return render(request,'core/galeria.html',{'lista':flores,'msg':msg})

@login_required(login_url='/login/')
def carrito(request):
    lista=request.session.get("carro","")
    arr=lista.split(";")
    return render(request,"core/carrito.html",{'lista':arr})

def vacio_carrito(request):
    request.session["carro"]=""
    lista=request.session.get("carro","")
    return render(request,"core/carrito.html",{'lista':lista})