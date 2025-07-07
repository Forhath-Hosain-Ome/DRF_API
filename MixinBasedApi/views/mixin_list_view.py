from rest_framework import mixins, generics
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from BaseModel.models import TeacherModel
from BaseSerializer.serializers import TeacherSerializers

class mixi(mixins.CreateModelMixin):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers