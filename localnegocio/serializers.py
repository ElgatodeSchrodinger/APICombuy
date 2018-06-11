from rest_framework import serializers
from localnegocio.models import Localnegocio,Productolocal, Users,Cliente

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

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ("remember_token","created_at","updated_at")

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'