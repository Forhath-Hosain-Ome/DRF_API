from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Model_App.models import CourseModel
from Serializer_App.serializer import CourseSerializer

class CourseEditView(APIView):            
    def get(self, request, pk):
        queryset = CourseModel.objects.get(pk=pk)
        serializer_class = CourseSerializer(queryset)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        queryset = CourseModel.objects.get(pk=pk)
        serializer = CourseSerializer(instance = queryset, data = request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def patch(self, request, pk):
        queryset = CourseModel.objects.get(pk=pk)
        serializer = CourseSerializer(instance = queryset, data = request.data, patrial = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, pk):
        queryset = CourseModel.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_410_GONE)
