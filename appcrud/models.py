from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Aerolineas(models.Model):
    id_aerolinea = models.AutoField(primary_key=True)
    nombre_aerolinea = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

class Aeropuertos(models.Model):
    id_aeropuerto = models.AutoField(primary_key=True)
    nombre_aeropuerto = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

class Movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

class Vuelos(models.Model):
    id_vuelo = models.AutoField(primary_key=True)
    id_aerolinea = models.ForeignKey(Aerolineas, on_delete=models.CASCADE)
    id_aeropuerto = models.ForeignKey(Aeropuertos, on_delete=models.CASCADE)
    id_movimiento = models.ForeignKey(Movimientos, on_delete=models.CASCADE)
    dia = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)




