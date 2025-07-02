from BaseModel.models import StudentModels
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentModels
        fields = '__all__'