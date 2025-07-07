from BaseModel.models import StudentModels
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModels
        fields = '__all__'