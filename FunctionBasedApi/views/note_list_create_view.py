from rest_framework.response import Response
from rest_framework.decorators import api_view
from BaseModel.models import NotesModel
from BaseSerializer.serializers import NoteSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def ApiFunctionView(request):
    if request.method == 'GET':
        note = NotesModel.objects.all()
        serializer = NoteSerializer(note, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)