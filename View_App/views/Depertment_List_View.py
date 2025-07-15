from rest_framework import generics
from Model_App.models import DepertmentModel
from Serializer_App.serializer import DepertmentSerializer

class DepertmentListView(generics.ListCreateAPIView):
    queryset = DepertmentModel.objects.all()
    serializer_class = DepertmentSerializer