from rest_framework.decorators import APIView
from BaseModel.models import StudentModels
from BaseSerializer.serializer import StudentSerializers
from rest_framework.response import Response
from rest_framework import status

class StudentView(APIView):
    def get(self, request):
        student = StudentModels.objects.all()
        serializer = StudentSerializers(student, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)