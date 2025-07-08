from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import NotesModel
from core.serializers import NoteSerializer
from rest_framework import status
        
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def ApiFunctionEdit(request, pk):
    note = NotesModel.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = NoteSerializer(note, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)