from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from Model_App.models import CourseModel
from Serializer_App.serializer import CourseSerializer

class CourseListView(APIView):
    def get(self,request):
        queryset = CourseModel.objects.all()
        serializer_class = CourseSerializer(queryset, many = True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer_class = CourseSerializer(data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)