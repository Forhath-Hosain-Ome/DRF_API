from rest_framework.decorators import api_view
from Model_App.models import AccountModel
from Serializer_App.serializer import AccountSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def AccountListView(request):
    if request.method == 'GET':
        model = AccountModel.objects.all()
        serializer = AccountSerializer(model, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)