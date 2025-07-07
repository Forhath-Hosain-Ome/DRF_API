from BaseSerializer.serializers import TeacherSerializers
from BaseModel.models import TeacherModel
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class TeacherEdit(GenericAPIView):
    queryset = Teacher.objects.get()
    serializer_class = TeacherSerializers


    def get(self, request, pk):
        teacher = self.get_object()
        serializer = self.get_serializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = self.get_queryset()
        serializer = self.get_serializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        teacher = self.get_queryset()
        serializer = self.get_serializer(teacher, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        teacher = self.get_queryset()
        if teacher is not None:
            teacher.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)