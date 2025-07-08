from rest_framework.decorators import APIView
# from BaseModel.models import StudentModels
# from BaseSerializer.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from core.models import StudentModels
from core.serializers import StudentSerializer


class StudentView(APIView):
    def get(self, request):
        student = StudentModels.objects.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)