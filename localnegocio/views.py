from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from localnegocio.models import Localnegocio
from localnegocio.serializers import LocalNegocioSerializer

@api_view(['GET', 'POST'])
def localnegocio_list(request):
    """
    List all code snippets, or create a new snippet.
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
    Retrieve, update or delete a code snippet.
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