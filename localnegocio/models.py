# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admnegocio(models.Model):
    idnegocio = models.ForeignKey('Localnegocio', models.DO_NOTHING, db_column='idnegocio')
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'admnegocio'


class Cliente(models.Model):
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'cliente'


class Disponibilidadprofesional(models.Model):
    idnegocio = models.ForeignKey('Localnegocio', models.DO_NOTHING, db_column='idnegocio')
    idprofesionales = models.ForeignKey('Profesionales', models.DO_NOTHING, db_column='idprofesionales')
    dia = models.CharField(max_length=1)
    horainicio = models.CharField(max_length=2, blank=True, null=True)
    horafin = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disponibilidadprofesional'


class Empresa(models.Model):
    nombreempresa = models.CharField(max_length=45)
    ruc = models.CharField(max_length=11)
    telefono = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'empresa'


class Localnegocio(models.Model):
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idempresa')
    latitud = models.FloatField()
    longitud = models.FloatField()
    descripcion = models.CharField(max_length=80, blank=True, null=True)
    telefono = models.CharField(max_length=9)
    hora_inicio = models.CharField(max_length=2)
    hora_fin = models.CharField(max_length=2)
    atencionestado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'localnegocio'


class Menu(models.Model):
    idnegocio = models.ForeignKey(Localnegocio, models.DO_NOTHING, db_column='idnegocio')
    plato = models.CharField(max_length=45)
    precio = models.CharField(max_length=45)
    disponible = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'menu'


class Pedidomenu(models.Model):
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idcliente')
    idmenu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='idmenu')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pedidomenu'


class Pedidoproducto(models.Model):
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idcliente')
    idproductolocal = models.ForeignKey('Productolocal', models.DO_NOTHING, db_column='idproductolocal')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pedidoproducto'


class Productolocal(models.Model):
    idnegocio = models.ForeignKey(Localnegocio, models.DO_NOTHING, db_column='idnegocio')
    nomproducto = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.IntegerField()
    marca = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productolocal'


class Profesionales(models.Model):
    nomprofesional = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'profesionales'


class Serviciolocal(models.Model):
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    idnegocio = models.ForeignKey(Localnegocio, models.DO_NOTHING, db_column='idnegocio')
    idtiposervicio = models.ForeignKey('Tiposervicio', models.DO_NOTHING, db_column='idtiposervicio')

    class Meta:
        managed = False
        db_table = 'serviciolocal'


class Tipolocal(models.Model):
    tiponegocio = models.ForeignKey('Tiponegocio', models.DO_NOTHING, db_column='tiponegocio')
    idlocal = models.ForeignKey(Localnegocio, models.DO_NOTHING, db_column='idlocal')

    class Meta:
        managed = False
        db_table = 'tipolocal'


class Tiponegocio(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tiponegocio'


class Tiposervicio(models.Model):
    nombretiposervicio = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tiposervicio'


class Usuario(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    dni = models.CharField(max_length=9)
    correo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'usuario'
