from rest_framework import generics
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from Model_App.models import SubjectModel
from Serializer_App.serializer import SubjectSerializer
from rest_framework.permissions import IsAuthenticated

class SubjectEditView(UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)