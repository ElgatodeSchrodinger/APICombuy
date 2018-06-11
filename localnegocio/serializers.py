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
        fields = ('id','name','lastname','role','dni','username','password','email')
