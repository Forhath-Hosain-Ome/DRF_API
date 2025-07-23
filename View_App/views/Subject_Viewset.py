from rest_framework.viewsets import ModelViewSet
from Model_App.models import SubjectModel
from Serializer_App.serializer import SubjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class SubjectViewSet(ModelViewSet):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    permission_classes = [IsAuthenticated]

    @action(detail = True, methods = ['POST'])
    def empty(self, request, pk=None):
        subject = self.get__object()
        subject.title = 'k'
        subject.save()
        return Response({'status': 'title updated', 'new_title': subject.title})

    @action(detail = False, methods = ['GET'])
    def empty(self, request, pk=None):
        subject = self.get__object(pk=1)
        return Response({subject.title})
