from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializers


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        Serializers = NoteSerializers(data=request.data)
        return Response(Serializers)
    elif request.method == 'GET':
        Serializers = NoteSerializers()
        return Response(Serializers)