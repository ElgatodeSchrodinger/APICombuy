# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    idusuario = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'administrador'


class Admnegocio(models.Model):
    idlocalnegocio = models.ForeignKey('Localnegocio', on_delete=models.CASCADE, db_column='idlocalnegocio')
    idusuario = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'admnegocio'


class Cliente(models.Model):
    idusuario = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'cliente'


class Localnegocio(models.Model):
    nombrenegocio = models.CharField(max_length=40)
    ruc = models.CharField(max_length=10)
    latitud = models.FloatField()
    longitud = models.FloatField()
    descripcion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=9)
    hora_inicio = models.CharField(max_length=5)
    hora_fin = models.CharField(max_length=5)
    idtiponegocio = models.ForeignKey('Tiponegocio', on_delete=models.CASCADE, db_column='idtiponegocio')

    class Meta:
        managed = False
        db_table = 'localnegocio'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Pedidoproducto(models.Model):
    cantidad = models.IntegerField()
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='idcliente')
    idprodnegocios = models.ForeignKey('Prodnegocios', on_delete=models.CASCADE, db_column='idprodnegocios')

    class Meta:
        managed = False
        db_table = 'pedidoproducto'


class Prodnegocios(models.Model):
    idlocalnegocio = models.ForeignKey(Localnegocio, on_delete=models.CASCADE, db_column='idlocalnegocio')
    idproductolocal = models.ForeignKey('Productolocal', on_delete=models.CASCADE, db_column='idproductolocal')
    precio = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prodnegocios'


class Productolocal(models.Model):
    nomproducto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    idtipolocalproducto = models.ForeignKey('Tipolocalproducto', on_delete=models.CASCADE, db_column='idtipolocalproducto')
    idtipoproducto = models.ForeignKey('Tipoproducto', on_delete=models.CASCADE, db_column='idtipoproducto')
    etiqueta = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'productolocal'


class Sugerencia(models.Model):
    nomproducto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    idtipolocalproducto = models.ForeignKey('Tipolocalproducto', on_delete=models.CASCADE, db_column='idtipolocalproducto')
    idtipoproducto = models.ForeignKey('Tipoproducto', on_delete=models.CASCADE, db_column='idtipoproducto')

    class Meta:
        managed = False
        db_table = 'sugerencia'


class Tipolocalproducto(models.Model):
    nombre = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipolocalproducto'


class Tiponegocio(models.Model):
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tiponegocio'


class Tipoproducto(models.Model):
    nomtipo = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'tipoproducto'


class Users(models.Model):
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    dni = models.CharField(unique=True, max_length=9)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=45)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
