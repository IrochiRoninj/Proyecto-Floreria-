from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def galeria(request):
    flores=Flores.objects.all()
    return render(request, 'core/galeria.html',{'listaflores':flores})    
