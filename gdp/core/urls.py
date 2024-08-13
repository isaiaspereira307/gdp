from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HonorariosViewSet, ProcessoViewSet

router = DefaultRouter()
router.register(r'honorarios', HonorariosViewSet)
router.register(r'processos', ProcessoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]