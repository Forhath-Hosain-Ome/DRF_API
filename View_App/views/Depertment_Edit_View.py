from rest_framework import generics
from Model_App.models import DepertmentModel
from Serializer_App.serializer import DepertmentSerializer
from rest_framework.permissions import IsAuthenticated

class DepertmentEditView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DepertmentModel.objects.all()
    serializer_class = DepertmentSerializer