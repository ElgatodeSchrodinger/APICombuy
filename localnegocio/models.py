from django.db import models

# Create your models here.

class localnegocio(models.Model):
	idNegocio=models.IntegerField(primary_key=True)
	latitud=models.FloatField()
	longitud=models.FloatField()
	descripcion=models.TextField()

	class Meta:
		ordering=("idNegocio",)