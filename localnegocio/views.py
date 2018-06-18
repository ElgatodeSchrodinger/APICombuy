from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from localnegocio.models import Localnegocio,Productolocal,Prodnegocios,Users
from localnegocio.serializers import LocalNegocioSerializer,ProductolocalSerializer,UsersSerializer,ProdnegocioSerializer


@api_view(['GET', 'POST'])
def localnegocio_list(request):
    """
    List all code Localnegocio, or create a new Localnegocio.
    """
    if request.method == 'GET':
        local = Localnegocio.objects.all()
        serializer = LocalNegocioSerializer(local, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LocalNegocioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def localnegocio_detail(request, pk):
    """
    Retrieve, update or delete a code Localnegocio.
    """
    try:
        localnegocio = Localnegocio.objects.get(pk=pk)
    except localnegocio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocalNegocioSerializer(localnegocio)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LocalNegocioSerializer(localnegocio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        localnegocio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def productos_list(request):
    """
    List all code Productolocal, or create a new Productolocal.
    """
    if request.method == 'GET':
        productos = Productolocal.objects.all()
        serializer = ProductolocalSerializer(productos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductolocalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def buscarproducto(request,nomproducto):
    """
    Busca Locales por producto.
    """
    try:
        producto = Productolocal.objects.filter(nomproducto__icontains=nomproducto) | Productolocal.objects.filter(etiqueta__icontains=nomproducto)
        negocios = []
        for n in producto:
            prodnegocios = Prodnegocios.objects.filter(idproductolocal=n.id)
            for i in prodnegocios:
                negocios.append(Localnegocio.objects.get(id=i.id))
        if not bool(negocios):
            return Response(status=status.HTTP_404_NOT_FOUND)
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LocalNegocioSerializer(negocios, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def login(request,username,password):
    try:
        usuario = Users.objects.get(username=username,password=password,role='user')
    except usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UsersSerializer(usuario)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    usuario=Users()
    try:
        usuario = Users.objects.get(username=request.data['username'],role='user')
    except usuario.DoesNotExist:
        if request.method == 'POST':
            serializer = UsersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'],['DELETE'])
def login_update(request,pk):
    try:
        usuario = Users.objects.get(pk=pk)
    except usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)        
    if request.method == 'PUT':
        serializer = UsersSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def valid(request,username):
    usuario=Users()
    try:
        usuario = Users.objects.get(username=username)
    except usuario.DoesNotExist:
        return Response({'message':'Nombre de usuario valido n.n'})
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def item(request,nomprod):
    producto=Productolocal()
    items=[]
    try:
        producto = Productolocal.objects.filter(nomproducto__icontains=nomprod) | Productolocal.objects.filter(etiqueta__icontains=nomprod)
        for n in producto:
            try:
                items.append(Prodnegocios.objects.get(idproductolocal=n.id))
            except Prodnegocios.DoesNotExist:
                pass
        if not bool(items):
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Productolocal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProdnegocioSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def listitem(request):
    prodnegocios= Prodnegocios()
    try:
        prodnegocios = Prodnegocios.objects.all()
    except prodnegocios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProdnegocioSerializer(prodnegocios, many=True)
        return Response(serializer.data)