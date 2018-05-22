# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admnegocio(models.Model):
    idadmnegocio = models.IntegerField(db_column='idAdmNegocio', primary_key=True)  # Field name made lowercase.
    idnegocio = models.IntegerField(db_column='idNegocio')  # Field name made lowercase.
    usuario_idusuario = models.IntegerField(db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admnegocio'


class Caracteristica(models.Model):
    idcarprod = models.IntegerField(db_column='idCarProd', primary_key=True)  # Field name made lowercase.
    caracteristica = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caracteristica'


class Cliente(models.Model):
    idcliente = models.IntegerField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    usuario_idusuario = models.IntegerField(db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Empresa(models.Model):
    idempresa = models.IntegerField(db_column='idEmpresa', primary_key=True)  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='nombreEmpresa', max_length=45)  # Field name made lowercase.
    ruc = models.CharField(db_column='RUC', max_length=11)  # Field name made lowercase.
    telefono = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'empresa'


class Localnegocio(models.Model):
    idnegocio = models.IntegerField(db_column='idNegocio', primary_key=True)  # Field name made lowercase.
    latitud = models.DecimalField(db_column='Latitud', max_digits=10, decimal_places=2)  # Field name made lowercase.
    longitud = models.DecimalField(db_column='Longitud', max_digits=10, decimal_places=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=80, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=9)  # Field name made lowercase.
    hora_inicio = models.CharField(db_column='Hora_inicio', max_length=2)  # Field name made lowercase.
    hora_fin = models.CharField(db_column='Hora_fin', max_length=2)  # Field name made lowercase.
    atencionestado = models.CharField(db_column='atencionEstado', max_length=1, blank=True, null=True)  # Field name made lowercase.
    localnegociocol = models.CharField(db_column='LocalNegociocol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tiponegocio_idtiponegocio = models.IntegerField(db_column='TipoNegocio_idTipoNegocio')  # Field name made lowercase.
    empresa_idempresa = models.IntegerField(db_column='Empresa_idEmpresa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localnegocio'


class Marca(models.Model):
    idproducto_caract = models.IntegerField(db_column='idProducto_Caract', primary_key=True)  # Field name made lowercase.
    nombre_marca = models.CharField(db_column='nombre_Marca', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marca'


class Menu(models.Model):
    idmenu = models.IntegerField(db_column='idMenu', primary_key=True)  # Field name made lowercase.
    plato = models.CharField(db_column='Plato', max_length=45)  # Field name made lowercase.
    precio = models.CharField(db_column='Precio', max_length=45)  # Field name made lowercase.
    disponible = models.CharField(db_column='Disponible', max_length=1)  # Field name made lowercase.
    idnegocio = models.IntegerField(db_column='idNegocio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'


class Pedidoproducto(models.Model):
    idventahistorial = models.IntegerField(db_column='idVentaHistorial', primary_key=True)  # Field name made lowercase.
    cliente_idcliente = models.IntegerField(db_column='Cliente_idCliente')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    productolocal_idproductolocal = models.IntegerField(db_column='ProductoLocal_idProductoLocal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedidoproducto'


class Producto(models.Model):
    idproducto = models.IntegerField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nom_producto = models.CharField(db_column='Nom_producto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipoprod_idtipoprod = models.IntegerField(db_column='TipoProd_idTipoProd')  # Field name made lowercase.
    marca_idproducto_caract = models.IntegerField(db_column='Marca_idProducto_Caract')  # Field name made lowercase.
    caracteristica_idcarprod = models.IntegerField(db_column='Caracteristica_idCarProd')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class Productolocal(models.Model):
    idproductolocal = models.IntegerField(db_column='idProductoLocal', primary_key=True)  # Field name made lowercase.
    precio = models.IntegerField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.
    localnegocio_idnegocio = models.IntegerField(db_column='LocalNegocio_idNegocio')  # Field name made lowercase.
    producto_idproducto = models.IntegerField(db_column='Producto_idProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productolocal'


class Productostock(models.Model):
    idproductostock = models.IntegerField(db_column='idProductoStock', primary_key=True)  # Field name made lowercase.
    stock = models.IntegerField()
    productolocal_idproductolocal = models.IntegerField(db_column='ProductoLocal_idProductoLocal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productostock'


class Serviciolocal(models.Model):
    idservicio = models.IntegerField(db_column='idServicio', primary_key=True)  # Field name made lowercase.
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    idnegocio = models.IntegerField(db_column='idNegocio')  # Field name made lowercase.
    tiposervicio_idtiposervicio = models.IntegerField(db_column='TipoServicio_idTipoServicio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serviciolocal'


class Tiponegocio(models.Model):
    idtiponegocio = models.IntegerField(db_column='idTipoNegocio', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiponegocio'


class Tipoprod(models.Model):
    idtipoprod = models.IntegerField(db_column='idTipoProd', primary_key=True)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='NombreProducto', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoprod'


class Tiposervicio(models.Model):
    idtiposervicio = models.IntegerField(db_column='idTipoServicio', primary_key=True)  # Field name made lowercase.
    nombretiposervicio = models.CharField(db_column='nombreTipoServicio', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiposervicio'


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    dni = models.CharField(max_length=9)
    correo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'usuario'
