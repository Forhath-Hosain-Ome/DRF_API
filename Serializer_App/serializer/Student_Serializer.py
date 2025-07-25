from Model_App.models import StudentEnrollment
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnrollment
        fields = '__all__'