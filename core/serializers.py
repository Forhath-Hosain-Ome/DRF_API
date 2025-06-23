from .models import note
from rest_framework import serializers

class NoteSerializers(serializers.ModelSerializer):
    class MEta:
        model = note
        fields = ['title','content']