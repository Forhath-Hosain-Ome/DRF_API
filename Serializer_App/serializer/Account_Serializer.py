from rest_framework import serializers
from Model_App.models import AccountModel

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ['name','phone_number','email']
        # fields = ['name', 'phone_number', 'email']
        # fields = '__all__'