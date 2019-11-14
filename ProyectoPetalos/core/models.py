from django.db import models

# Create your models here.
class Flores(models.Model):
    fotografia=models.ImageField(upload_to="flores",null=True)
    name=models.CharField(max_length=100, primary_key=True)
    valor=models.IntegerField()
    descripcion=models.TextField()
    estado=models.BooleanField()
    stock=models.IntegerField()

    def __str__(self):
        return self.name
