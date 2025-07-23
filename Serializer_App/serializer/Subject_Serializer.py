from rest_framework import serializers
from Model_App.models import SubjectModel

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = '__all__'