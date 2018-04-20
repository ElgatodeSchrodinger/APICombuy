from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from localnegocio.models import Localnegocio
from localnegocio.serializers import LocalNegocioSerializer

@csrf_exempt
def localnegocio_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        local = Localnegocio.objects.all()
        serializer = LocalNegocioSerializer(local, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocalNegocioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def localnegocio_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        localnegocio = Localnegocio.objects.get(pk=pk)
    except localnegocio.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LocalNegocioSerializer(localnegocio)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LocalnegocioSerializer(localnegocio, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        localnegocio.delete()
        return HttpResponse(status=204)