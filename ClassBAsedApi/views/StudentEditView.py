from rest_framework.decorators import APIView
from BaseModel.models import StudentModels
from BaseSerializer.serializer import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404



class StudentEdit(APIView):
    def get_object(self, pk):
        try:
            student = StudentModels.objects.get(pk = pk)
        except StudentModels.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializers(student)
        return Response(serializer.data)
    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializers(student, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)