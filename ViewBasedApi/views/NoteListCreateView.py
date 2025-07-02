from rest_framework.response import Response
from rest_framework.decorators import api_view
from BaseModel.models import Notes
from BaseSerializer.serializer import NoteSerializers
from rest_framework import status

@api_view(['GET', 'POST'])
def ApiFunctionView(request):
    if request.method == 'GET':
        note = Notes.objects.all()
        serializer = NoteSerializers(note, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NoteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)