from BaseSerializer.serializers import TeacherSerializers
from BaseModel.models import TeacherModel
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class TeacherView(GenericAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers

    def get(self, request):
        teacher = self.get_queryset()
        serializer = self.get_serializer(teacher, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)