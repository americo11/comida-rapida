from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField( max_length=200 , help_text='ingrese el nombre??¡???')

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    fecha_nacimiento = models.DateField('fecha de nacimeinto ', null=True, blank=True)
    fecha_muerte = models.DateField('fecha de fallecimientyo ', null=True ,blank = True)


class meta:
    ordering =['apellido', 'nombre']

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

    def get_absolute_url(self):
        return reverse("autor-detalle", args=[str(self.id)])
        





class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    resumen = models.TextField(max_length=200, help_text='ingresa brebe descripcion' )
    isbn =  models.CharField('ISBN', max_length=13, help_text='15 cacracteres ')
    genero = models.ManyToManyField('genero' , help_text='seeleccione el genero ')

    def __str__(self):
        return self.titulo


    def get_absolute_url(self):
        return reverse("libro-detalle", args=[str(self.id)])




class idioma(models.Model):
    nombre= models.CharField( max_length=50 , help_text='ingrese el idioma')

    def __str__(self):
        return self.nombre
    



    


class inventario(models.Model):
    ESTADO_PRESTAMO = (
('m', 'Mantenimiento'),
('p', 'prestamo'),
('d', 'disponible'),
('r', 'reservado')
)

    id  = models.UUIDField(primary_key=True , default=uuid.uuid4, help_text='unico')
    #id = models.UUIDField(primary_Key=True, default=uuid.uuid4, help_text=' unico para este comentario ')
    Libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
#   libro = models.ForeignKey(libro, on_delete=models.SET_NULL, null=True)
    idioma = models.ForeignKey(idioma, on_delete=models.SET_NULL, null=True)
    impreso = models.CharField(max_length=200)
    devolucion = models.DateField(null=True, blank=True)
    estatus = models.CharField(max_length=10, choices=ESTADO_PRESTAMO,blank=True, default='m' , help_text='disponibilidad ')



class meta:
    ordering: ['devolucion  '] 

    def __str__(self):
        return f'{self.id (self.libro.titulo)}'
    