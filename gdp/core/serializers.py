from rest_framework import serializers
from .models import Honorarios, Processo

class HonorariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honorarios
        fields = '__all__'

class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = '__all__'