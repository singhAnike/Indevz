from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone', 'company_name', 'access_code']
        extra_kwargs = {'password': {'write_only': True}}
