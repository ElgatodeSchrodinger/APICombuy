from rest_framework import serializers
from localnegocio.models import Localnegocio


class LocalNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localnegocio
        fields = ('idNegocio', 'latitud', 'longitud', 'descripcion')