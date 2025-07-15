from Model_App.models import DepertmentModel
from rest_framework import serializers

class DepertmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepertmentModel
        fields = '__all__'