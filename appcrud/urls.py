from rest_framework import routers
from .api import AerolineasViewSet, AeropuertosViewSet, MovimientosViewSet, VuelosViewSet
from django.urls import path, include
from .views import ExternalDataView, TotalAnsweredView, MaxReputationView, MinViewCountView, AnswerTimeView, VuelosConAeropuertosView, AerolineaMasVuelosView, DiasConMayorVuelosView, MasDeDosVuelosPorDiaView

router = routers.DefaultRouter()

router.register('api/aerolineas', AerolineasViewSet,'aerolineas')
router.register('api/aeropuertos', AeropuertosViewSet,'aeropuertos')
router.register('api/movimientos', MovimientosViewSet,'movimientos')
router.register('api/vuelos', VuelosViewSet,'vuelos')

urlpatterns = [
    path('', include(router.urls)),
    path('api/external/', ExternalDataView.as_view(), name='externaldata'),
    path('api/answered/', TotalAnsweredView.as_view(), name='Answered'),
    path('api/reputation/', MaxReputationView.as_view(), name='Reputation'),
    path('api/minview/', MinViewCountView.as_view(), name='MinView'),
    path('api/current/', AnswerTimeView.as_view(), name='current'),
    path('api/vuelosconaeropuertos/', VuelosConAeropuertosView.as_view(), name='vuelosconaeropuertos'),
    path('api/aerolineamasvuelos/', AerolineaMasVuelosView.as_view(), name='aerolineamasvuelos'),
    path('api/diasconmayorvuelos/', DiasConMayorVuelosView.as_view(), name='diasconmayorvuelos'),
    path('api/masdedosvuelospordia/', MasDeDosVuelosPorDiaView.as_view(), name='masdedosvuelospordia'),
    
]
