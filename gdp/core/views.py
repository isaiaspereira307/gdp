from rest_framework import viewsets
from .models import Honorarios, Processo
from .serializers import HonorariosSerializer, ProcessoSerializer

class HonorariosViewSet(viewsets.ModelViewSet):
    queryset = Honorarios.objects.all()
    serializer_class = HonorariosSerializer

class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer