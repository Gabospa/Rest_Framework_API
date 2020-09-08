from django.shortcuts import render
from rest_framework import generics, status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import Persona
from .serializer import PersonaSerializer

# Function based views
@api_view(['GET', 'POST'])
def person_list(request):
    # Function GET  all users
    if request.method == 'GET':
        personas = Persona.objects.all()
        username = request.GET.get('username', None)
        if username is not None:
            personas = personas.filter(title__icontains=username)
        personas_serializer = PersonaSerializer(personas, many=True)
        return JsonResponse(personas_serializer.data, safe=False)

    # Function POST new user
    elif request.method == 'POST':
        person_data = JSONParser().parse(request)
        person_serializer = PersonaSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, pk):
    #  Find album by id
    try:
        person = Persona.objects.get(pk=pk)
    except Persona.DoesNotExist:
        return JsonResponse({'message': 'El id no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    # GET a single album
    if request.method == 'GET':
        person_serializer = PersonaSerializer(person)
        return JsonResponse(person_serializer.data)

    # PUT on a single album
    elif request.method == 'PUT':
        person_data = JSONParser().parse(request)
        person_serializer = PersonaSerializer(person, data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data)
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE a single album
    elif request.method == 'DELETE':
        person.delete()
        return JsonResponse({'message': 'El usuario ha sido borrado'}, status=status.HTTP_204_NO_CONTENT)




"""
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
"""
