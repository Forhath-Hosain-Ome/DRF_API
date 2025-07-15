from rest_framework.decorators import api_view
from Model_App.models import AccountModel
from Serializer_App.serializer import AccountSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def AccountListView(request):
    if request.method == 'GET':
        queryset = AccountModel.objects.all()
        serializer_class = AccountSerializer(queryset, many = True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer_class = AccountSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)