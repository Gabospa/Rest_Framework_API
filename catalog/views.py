from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Album, Track
from .serializer import AlbumSerializer

# Function based views
@api_view(['GET', 'POST'])
def album_list(request):
    
    #Function to GET all albums
    if request.method == 'GET':
        albums = Album.objects.all()
        title = request.GET.get('album_name', None)
        if title is not None:
            albums = albums.filter(title__icontains=title)
        
        albums_serializer = AlbumSerializer(albums, many=True)
        return JsonResponse(albums_serializer.data, safe=False)
    
    # Function to POST new album
    elif request.method == 'POST':
        album_data = JSONParser().parse(request)
        album_serializer = AlbumSerializer(data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse(album_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(album_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, pk):
    #Find album by id (pk)
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return JsonResponse({'message': 'El album no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    # Function to GET a single album
    if request.method == 'GET':
        album_serializer = AlbumSerializer(album)
        return JsonResponse(album_serializer.data)
    
    # Function to PUT a single album
    elif request.method == 'PUT':
        album_data = JSONParser().parse(request)
        album_serializer = AlbumSerializer(album, data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse(album_serializer.data)
        return JsonResponse(album_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Function to DELETE a single album
    elif request.method == 'DELETE':
        album.delete()
        return JsonResponse({'message':'El album ha sido borrado'}, status=status.HTTP_204_NO_CONTENT)