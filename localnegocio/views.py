from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from localnegocio.models import Localnegocio,Productolocal
from localnegocio.serializers import LocalNegocioSerializer,ProductolocalSerializer


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
def localproductos_list(request):
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
def localesporproductos_list(request,nomproducto):
    """
    List all code Productolocal, or create a new Productolocal.
    """
    prodnegocios=[]
    try:
        producto = Productolocal.objects.get(nomproducto=nomproducto)
        prodnegocios = Prodnegocios.objects.filter(idproductolocal=producto.id)
        negocios = []
        for i in prodnegocios:
            negocios.append(Localnegocio.objects.get(id=i.idlocalnegocio))
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except prodnegocios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except negocios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = LocalNegocioSerializer(negocios, many=True)
    return Response(serializer.data)
