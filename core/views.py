# class basd 
from rest_framework import status
from .models import note
from .serializers import NoteSerializers
from rest_framework import generics


class Notes_List(generics.ListCreateAPIView):
    queryset = note.objects.all()
    serializer_class = NoteSerializers

class Note_Edit(generics.RetrieveUpdateDestroyAPIView):
    queryset = note.objects.all()
    serializer_class = NoteSerializers


# Function based


# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import note
# from .serializers import NoteSerializers


# @api_view(['GET', 'POST'])
# def notes_create(request):
#     if request.method == 'GET':
#         notes = note.objects.all()
#         Serializer = NoteSerializers(notes, many = True)
#         return Response(Serializer.data)
#     elif request.method == 'POST':
#         Serializer = NoteSerializers(data = request.data, many=True)
#         if Serializer.is_valid():
#             Serializer.save()
#             return Response(Serializer.data, status = status.HTTP_200_OK)
#         return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def notes_create_details(request,pk):
#     try:
#         notes = note.objects.get(pk=pk)
#     except:
#         return Response({'message' : 'note not found'}, status= status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = NoteSerializers(notes)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer = NoteSerializers(notes, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         notes.delete()
#         return Response({'message':'note deleted'}, status=status.HTTP_200_OK)