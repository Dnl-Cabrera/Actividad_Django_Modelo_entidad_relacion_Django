from django.db import models
from usuario.models import Usuario
from matriculas.models import Matricula

# Create your models here.
'''
Ejemplo que se utilizo en la presentación.
from personal.models import Domicilio

class Torre(models.Model):
    #id_domicilio=models.ForeignKey(Domicilio,on_delete=models.CASCADE)
    #agregar el id no es necesario, django lo crea.
    Nombre=models.CharField(max_length=50,default='')
    id_Domicilio=models.ForeignKey(Domicilio,on_delete=models.CASCADE)

class Apartamento(models.Model):
    Nombre=models.CharField(max_length=50,default='')
'''
class Grado(models.Model):
    nombre=models.CharField(max_length=50,default='')
    estado_grado=models.CharField(max_length=50,default='')
    fecha_creacion=models.CharField(max_length=50,default='')

class Asignatura(models.Model):
    id_grado=models.ForeignKey(Grado,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50,default='')
    estado_asignatura=models.CharField(max_length=50,default='')
    fecha_creacion=models.CharField(max_length=50,default='')

class Cursos(models.Model):
    #id_lista_estudiantes=models.ForeignKey(Lista_estudiantes,on_delete=models.CASCADE)
    id_grado=models.ForeignKey(Grado,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50,default='')
    estado_curso=models.CharField(max_length=50,default='')
    fecha_creacion=models.CharField(max_length=50,default='')

class Lista_estudiante(models.Model):
    id_matricula=models.ForeignKey(Matricula,on_delete=models.CASCADE)
    id_curso=models.OneToOneField(Cursos,on_delete=models.CASCADE,primary_key=True)
    id_usuario_director_curso=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    #id_usuario_director_curso=models.OneToOneField(Usuario,on_delete=models.CASCADE,primary_key=True) #Se esta creando una relacion uno a uno, Preguntar como funciona el primary Key  
    estado_lista_estudiante=models.CharField(max_length=50,default='')
    fecha_creacion=models.CharField(max_length=50,default='')

class Carga_horaria(models.Model):
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    id_curos=models.ForeignKey(Cursos,on_delete=models.CASCADE)
    estado_carga_horaria=models.CharField(max_length=50,default='')
    fecha_creacion=models.CharField(max_length=50,default='')

class Notas_estudiantes_curso(models.Model):
    id_lista_estdiante=models.ForeignKey(Matricula,on_delete=models.CASCADE)
    id_asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    id_carga_horaria=models.OneToOneField(Carga_horaria,on_delete=models.CASCADE,primary_key=True)
    Nota=models.CharField(max_length=50,default='')
    fecha_creacion=models.CharField(max_length=50,default='')

class Area(models.Model):
    id_asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    id_usuario_jefe_area=models.OneToOneField(Usuario,on_delete=models.CASCADE,primary_key=True) #Se esta creando una relacion uno a uno, Preguntar como funciona el primary Key  
    nombre=models.CharField(max_length=50,default='')
    fecha_creacion=models.CharField(max_length=50,default='')
    estado_area=models.CharField(max_length=50,default='')



    