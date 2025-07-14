from rest_framework.decorators import api_view
from Model_App.models import AccountModel
from Serializer_App.serializer import AccountSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def AccountEditView(request, pk):
    model = AccountModel.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = AccountSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = AccountSerializer(data = request.data, instance = model)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = AccountSerializer(data = request.data, instance = model, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        model.delete()
        return Response(status=status.HTTP_410_GONE)