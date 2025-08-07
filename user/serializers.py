from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name','password', 'is_super_admin','is_active']
        read_only_fields = ['id', 'is_super_admin',] 
        extra_kwargs = {'password': {'write_only': True}}
