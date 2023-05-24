from django.db import models

# Create your models here.

class Acudientes(models.Model):
    #agregar el id no es necesario, django lo crea.
    cedula=models.CharField(max_length=50,default='',unique=True)
    nombre=models.CharField(max_length=50,default='')
    apellido=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    telefono=models.CharField(max_length=50,default='')
    estado_usuario=models.CharField(max_length=50,default='')
    fecha_creacion=models.CharField(max_length=50,default='')
    #Es para que autmaticamenrte muestre el nombre del modelo Pais cuando se haga alguna referencia, ej: en estado que tiene el id_pais.
    def __str__(self):
        return self.cedula
    
class Estudiantes(models.Model):
    identificacion=models.CharField(max_length=50,default='',unique=True)
    nombre=models.CharField(max_length=50,default='')
    apellido=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    telefono=models.CharField(max_length=50,default='')
    estado_estudiante=models.CharField(max_length=50,default='')
    fecha_creacion=models.CharField(max_length=50,default='')

class Matricula(models.Model):
    id_acudiente=models.ForeignKey(Acudientes,on_delete=models.CASCADE)
    id_estudiante=models.ForeignKey(Estudiantes,on_delete=models.CASCADE)
    grado=models.CharField(max_length=50,default='')
    estado_matricula=models.CharField(max_length=50,default='')
    fecha_matricula=models.CharField(max_length=50,default='')
