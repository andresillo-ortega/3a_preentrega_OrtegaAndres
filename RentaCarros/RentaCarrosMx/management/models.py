from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Carro(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.año})'

class Renta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    fecha_renta = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f'{self.cliente} - {self.carro}'