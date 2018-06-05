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
        
"""
    def create(self, validated_data):
        idLocalNegocio = validated_data.pop('')
        Productos = Productolocal.objects.get(idnegocio=idLocalNegocio['id'])
        empresa.objects.create(Productolocal=Productolocal, **empresa)
        return user
"""