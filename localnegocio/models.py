# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admnegocio(models.Model):
    idlocalnegocio = models.PositiveIntegerField()
    idusuario = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'admnegocio'


class Cliente(models.Model):
    idusuario = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Dia(models.Model):
    iddia = models.CharField(primary_key=True, max_length=1)
    nomdia = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'dia'


class Disponibilidadprofesional(models.Model):
    iddia = models.CharField(max_length=1)
    horainicio = models.CharField(max_length=2)
    horafin = models.CharField(max_length=2)
    idprofesionales = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'disponibilidadprofesional'


class Localnegocio(models.Model):
    nombrenegocio = models.CharField(max_length=40)
    ruc = models.CharField(max_length=10)
    latitud = models.FloatField()
    longitud = models.FloatField()
    descripcion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=9)
    hora_inicio = models.CharField(max_length=5)
    hora_fin = models.CharField(max_length=5)
    estado = models.CharField(max_length=1)
    idtiponegocio = models.PositiveIntegerField()

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
    idcliente = models.PositiveIntegerField()
    idprodnegocios = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pedidoproducto'


class Prodnegocios(models.Model):
    idlocalnegocio = models.PositiveIntegerField()
    idproductolocal = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prodnegocios'


class Productolocal(models.Model):
    nomproducto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    idtipolocalproducto = models.PositiveIntegerField()
    idtipoproducto = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'productolocal'


class Profesionales(models.Model):
    nomprofesional = models.CharField(max_length=45)
    correoprofesional = models.CharField(max_length=45)
    telefonoprofesional = models.CharField(max_length=9)
    idservicio = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesionales'


class Servicio(models.Model):
    idservicio = models.AutoField(primary_key=True)
    nomservico = models.CharField(max_length=45)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    idlocalnegocio = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'servicio'


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
