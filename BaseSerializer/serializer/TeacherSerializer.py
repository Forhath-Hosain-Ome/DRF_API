from rest_framework import serializers
from BaseModel.models import Teacher

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'