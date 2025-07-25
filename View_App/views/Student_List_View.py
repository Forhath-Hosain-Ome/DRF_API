from rest_framework import viewsets
from Serializer_App.serializer import StudentSerializer
from Model_App.models import StudentEnrollment


class StudentListView(viewsets.ViewSet):
    queryset = StudentEnrollment.objects.all()
    serializer_class = StudentSerializer