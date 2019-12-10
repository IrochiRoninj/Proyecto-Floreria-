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
    opinion=models.TextField()

    def __str__(self):
        return self.name