from BaseModel.models import Notes
from rest_framework import serializers

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'