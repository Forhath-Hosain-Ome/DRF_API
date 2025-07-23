from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from Model_App.models import SubjectModel
from Serializer_App.serializer import SubjectSerializer
from rest_framework.permissions import IsAuthenticated


class SubjectListView(CreateModelMixin, ListModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)