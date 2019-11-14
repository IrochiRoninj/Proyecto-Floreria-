from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def galeria(request):
    return render(request,'core/galeria.html')  

def quienes_somos(request):
    return render(request,'core/quienes_somos.html')    

def formulario(request):
    return render(request,'core/formulario.html')

def categoria(request):
    return render(request,'core/galeria')

def caja(request):
    return render(request,'core/galeria')

def novia_y_eventos(request):
    return render(request,'core/galeria')

def florero(request):
    return render(request,'core/galeria')   

def cerrar_sesion(request):
    return render(request,'core/login')    