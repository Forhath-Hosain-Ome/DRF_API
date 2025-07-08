from rest_framework import mixins, generics
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from core.serializers import TeacherSerializer
from core.models import TeacherModel

class mixi(mixins.CreateModelMixin):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer