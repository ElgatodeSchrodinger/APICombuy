# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admnegocio(models.Model):
    idlocalnegocio = models.ForeignKey('Localnegocio', models.DO_NOTHING, db_column='idlocalnegocio')
    idusuario = models.ForeignKey('Users', models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'admnegocio'


class Cliente(models.Model):
    idusuario = models.ForeignKey('Users', models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'cliente'


class Dia(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    nomdia = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'dia'


class Disponibilidadprofesional(models.Model):
    iddia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='iddia')
    horainicio = models.CharField(max_length=2)
    horafin = models.CharField(max_length=2)
    idprofesionales = models.ForeignKey('Profesionales', models.DO_NOTHING, db_column='idprofesionales')

    class Meta:
        managed = False
        db_table = 'disponibilidadprofesional'


class Localnegocio(models.Model):
    nombrenegocio = models.CharField(max_length=40)
    ruc = models.CharField(max_length=10, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    hora_inicio = models.CharField(max_length=5, blank=True, null=True)
    hora_fin = models.CharField(max_length=5, blank=True, null=True)
    idtiponegocio = models.ForeignKey('Tiponegocio', models.DO_NOTHING, db_column='idtiponegocio')

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
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idcliente')
    idprodnegocios = models.ForeignKey('Prodnegocios', models.DO_NOTHING, db_column='idprodnegocios')

    class Meta:
        managed = False
        db_table = 'pedidoproducto'


class Prodnegocios(models.Model):
    idlocalnegocio = models.ForeignKey(Localnegocio, models.DO_NOTHING, db_column='idlocalnegocio')
    idproductolocal = models.ForeignKey('Productolocal', models.DO_NOTHING, db_column='idproductolocal')
    precio = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prodnegocios'


class Productolocal(models.Model):
    nomproducto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    idtipolocalproducto = models.ForeignKey('Tipolocalproducto', models.DO_NOTHING, db_column='idtipolocalproducto')
    idtipoproducto = models.ForeignKey('Tipoproducto', models.DO_NOTHING, db_column='idtipoproducto')

    class Meta:
        managed = False
        db_table = 'productolocal'


class Profesionales(models.Model):
    nomprofesional = models.CharField(max_length=45)
    correoprofesional = models.CharField(max_length=45)
    telefonoprofesional = models.CharField(max_length=9)
    idservicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='idservicio')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesionales'


class Servicio(models.Model):
    nomservico = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'servicio'


class Serviciolocal(models.Model):
    idservicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='idservicio')
    idlocalnegocio = models.ForeignKey(Localnegocio, models.DO_NOTHING, db_column='idlocalnegocio')
    precio = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'serviciolocal'


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
