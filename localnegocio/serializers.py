from rest_framework import serializers
from localnegocio.models import Localnegocio,Productolocal

class ProductolocalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Productolocal
		exclude = ("id",)
		depth = 1


class LocalNegocioSerializer(serializers.ModelSerializer):
	#Productolocal= ProductolocalSerializer(required=false,many=True)

    class Meta:
        model = Localnegocio
        fields = '__all__'