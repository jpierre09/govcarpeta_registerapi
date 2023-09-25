from rest_framework import serializers
from .models import UserRegister

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = ('id', 'name', 'address', 'email', 'operatorId', 'operatorName')