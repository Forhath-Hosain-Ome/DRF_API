from BaseModel.models import NotesModel
from rest_framework import serializers

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesModel
        fields = '__all__'