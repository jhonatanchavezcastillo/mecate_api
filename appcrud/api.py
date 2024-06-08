from .models import Aerolineas, Aeropuertos, Movimientos, Vuelos
from rest_framework import viewsets, permissions
from .serializers import AerolineasSerializer, AeropuertosSerializer, MovimientosSerializer, VuelosSerializer

class AerolineasViewSet(viewsets.ModelViewSet):
    queryset = Aerolineas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AerolineasSerializer

class AeropuertosViewSet(viewsets.ModelViewSet):
    queryset = Aeropuertos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AeropuertosSerializer

class MovimientosViewSet(viewsets.ModelViewSet):
    queryset = Movimientos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MovimientosSerializer

class VuelosViewSet(viewsets.ModelViewSet):
    queryset = Vuelos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VuelosSerializer