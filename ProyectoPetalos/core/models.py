from django.db import models
 
class Flores(models.Model):
    imagen=models.ImageField(upload_to="flores",null=True)
    name=models.CharField(max_length=100, primary_key=True)
    precio=models.IntegerField()
    descripcion=models.TextField()
    estado=models.BooleanField()
    stock=models.IntegerField()

    def __str__(self):
        return self.name
        
class Opinion(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    op=models.TextField()

    def __str__(self):
        return self.name

class Boleta(models.Model):
    usuario=models.CharField(max_length=100)
    titulo=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    total=models.IntegerField()
    fecha=models.DateField()

    def __str__(self):
        return str(self.usuario)+' '+str(self.titulo)