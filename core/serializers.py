from .models import note
from rest_framework import serializers

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = note
        fields = ['pk','title','content','created_at']