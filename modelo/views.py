from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from modelo.serializers import Empleado, Direccion
from modelo.serializers import EmpleadoSerializer, DireccionSerializer

# Create your views here.

@csrf_exempt
def listApi(request, id=0):
    if request.method == 'GET':
        direccion = Direccion.objects.all()
        direccion_serializer=DireccionSerializer(direccion,many=True)
        return JsonResponse(direccion_serializer.data,safe=False)
    elif request.method=='POST':
        direccion_data=JSONParser().parse(request)
        direccion_serializer=DireccionSerializer(data=direccion_data)
        if direccion_serializer.is_valid():
            direccion_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        direccion_data=JSONParser().parse(request)
        direccion=Direccion.objects.get(direccionId=direccion_data['direccionId'])
        direccion_serializer=DireccionSerializer(direccion,data=direccion_data)
        if direccion_serializer.is_valid():
            direccion_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        direccion=Direccion.objects.get(direccionId=id)
        direccion.delete()
        return JsonResponse("Deleted Successfully",safe=False)