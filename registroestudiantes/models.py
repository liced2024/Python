from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Libro(models.Model):
    titulo = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 100)
    autor = models.CharField(max_length= 100)
    paginas = models.IntegerField(max_length=5)
    editorial = models.CharField(max_length= 100)


