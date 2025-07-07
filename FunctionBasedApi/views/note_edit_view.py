from rest_framework.response import Response
from rest_framework.decorators import api_view
from BaseModel.models import Notes
from BaseSerializer.serializers import NoteSerializers
from rest_framework import status
        
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def ApiFunctionEdit(request, pk):
    note = Notes.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = NoteSerializers(note)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = NoteSerializers(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = NoteSerializers(note, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)