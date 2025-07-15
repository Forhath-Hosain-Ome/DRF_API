from rest_framework.decorators import api_view
from Model_App.models import AccountModel
from Serializer_App.serializer import AccountSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def AccountEditView(request, pk):
    queryset = AccountModel.objects.get(pk=pk)
    if request.method == 'GET':
        serializer_class = AccountSerializer(queryset)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer_class = AccountSerializer(data = request.data, instance = queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer_class = AccountSerializer(data = request.data, instance = queryset, partial = True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_410_GONE)