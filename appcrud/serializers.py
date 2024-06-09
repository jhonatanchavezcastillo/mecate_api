from rest_framework import serializers 
from .models import Aerolineas, Aeropuertos, Movimientos, Vuelos

class AerolineasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aerolineas
        fields = ('id_aerolinea','nombre_aerolinea','create_at')
        read_only_fields = ('create_at', ) # definir campos de solo lectura

class AeropuertosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeropuertos
        #fields = ('id_aeropuerto','nombre_aeropuerto','create_at')
        fields = '__all__' 
        read_only_fields = ('create_at', ) # definir campos de solo lectura

class MovimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimientos
        fields = ('id_movimiento','descripcion','create_at')
        read_only_fields = ('create_at', ) # definir campos de solo lectura

class VuelosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelos
        #fields = ('id_vuelo','id_aerolinea','id_aeropuerto','id_movimiento','dia','create_at')
        fields = '__all__' 
        read_only_fields = ('create_at', ) # definir campos de solo lectura