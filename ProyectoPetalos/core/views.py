from django.shortcuts import render
from .models import Flores,Opinion,Boleta
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime
from .clases import elemento

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    return render(request,'core/index.html')

@login_required(login_url='/login/')
def galeria(request):
    flor=Flores.objects.all()
    return render(request,'core/galeria.html',{'lista':flor})  

@login_required(login_url='/login/')
def formulario(request):
    
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
        mensaje='Enviado'
        flores=Flores.objects.all() 
        return render(request,'core/formulario.html',{'lista':flores,'msg':'Se Guardo','sw':True})
    return render(request,'core/formulario.html')

@login_required(login_url='/login/')
def quienes_somos(request):
    return render(request,'core/quienes_somos.html')    

def login(request):
    return render(request,'core/login.html')

def login_iniciar(request):
    
    if request.POST:
        u=request.POST.get("txtUsuario")
        p=request.POST.get("txtPass")
        usu=authenticate(request,username=u,password=p)
        msg=''
        request.session["carritox"] = []
        request.session["carrito"] = []
        if usu is not None and usu.is_active:
            auth_login(request,usu)
            return render(request,'core/index.html')
    return render(request,'core/login.html',{'msg':msg})

def cerrar_sesion(request):
    logout(request)
    return HttpResponse("<script>alert('cerro sesion');window.location.href='/';</script>")


@login_required(login_url='/login/')
def carrito(request):
    lista=request.session["carritox"]
    suma=0
    for item in lista:
        suma=suma+int(item["total"])
    return render(request,"core/carrito.html",{'lista':lista,'total':suma})

@login_required(login_url='/login/')
def carro_compras(request,id):
    f=Flores.objects.get(name=id)
    x=request.session["carritox"]
    el=elemento(1,f.name,f.precio,1)
    sw=0
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            sw=1
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    if sw==0:
        clon.append(el.toString())
    x=clon    
    request.session["carritox"]=x
    flors=Flores.objects.all()    
    return render(request,'core/galeria.html',{'flores':flors,'total':suma})

@login_required(login_url='/login/')
def grabar_carro(request):
    x=request.session["carritox"]    
    usuario=request.user.username
    suma=0
    try:
        for item in x:        
            titulo=item["nombre"]
            precio=int(item["precio"])
            cantidad=int(item["cantidad"])
            total=int(item["total"])        
            boleta=Boleta(
                usuario=usuario,
                titulo=titulo,
                precio=precio,
                cantidad=cantidad,
                total=total,
                fecha=datetime.date.today()
            )
            boleta.save()
            suma=suma+int(total)  
            print("reg grabado")                 
        mensaje="Grabado"
        request.session["carritox"] = []
    except:
        mensaje="error al grabar"            
    return render(request,'core/carrito.html',{'x':x,'total':suma,'mensaje':mensaje})

@login_required(login_url='/login/')
def carro_compras_mas(request,id):
    f=Flores.objects.get(name=id)
    x=request.session["carritox"]
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]        
    return render(request,'core/carrito.html',{'x':x,'total':suma})

@login_required(login_url='/login/')
def carro_compras_menos(request,id):
    f=Flores.objects.get(name=id)
    x=request.session["carritox"]
    clon=[]
    suma=0
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            cantidad=int(cantidad)-1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total)
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]    
    return render(request,'core/carrito.html',{'x':x,'total':suma})    

#####################################################################
def isset(variable):
	return variable in locals() or variable in globals()    