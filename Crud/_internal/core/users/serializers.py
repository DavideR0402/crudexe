from rest_framework import serializers # type: ignore
from django.contrib.auth.models import User # type: ignore

class UserSerializer(serializers.ModelSerializer):
    
    """
        UserSerializer Class

        Serializer for user

    """
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    