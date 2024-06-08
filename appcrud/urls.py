from rest_framework import routers
from .api import AerolineasViewSet, AeropuertosViewSet, MovimientosViewSet, VuelosViewSet

router = routers.DefaultRouter()

router.register('api/aerolineas', AerolineasViewSet,'aerolineas')
router.register('api/aeropuertos', AeropuertosViewSet,'aeropuertos')
router.register('api/movimientos', MovimientosViewSet,'movimientos')
router.register('api/vuelos', VuelosViewSet,'vuelos')

urlpatterns = router.urls
