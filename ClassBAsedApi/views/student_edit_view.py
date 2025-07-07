from rest_framework.decorators import APIView
# from BaseModel.models import StudentModels
# from BaseSerializer.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from core.models.student_model_core import *


class StudentEdit(APIView):
    def get_object(self, pk):
        try:
            student = StudentModels.objects.get(pk = pk)
            return student
        except StudentModels.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        student = self.get_object(pk)
        if student is not None:
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)