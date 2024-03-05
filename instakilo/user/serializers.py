from rest_framework import serializers
from multiprocessing import Value
from multiprocessing.managers import ValueProxy
from optparse import Values
from typing import ValuesView
from rest_framework import serializers

import re 

class LoginSerializer(serializers.Serializer):
    """form for the login page

    Args:
        serializers (type): description
    """
    username = serializers.CharField()
    password = serializers.CharField()
    

class RegistrationSerializer(serializers.Serializer):
    name = serializers.CharField()
    emailid = serializers.EmailField()
    mobno = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_user_name(self, value):
        
        """Validate for the username."""
        if value == "":
            raise serializers.ValidationError("user name cannot be empty")
        if not any(character.isdigit() for character in value):
            raise serializers.ValidationError("must contain digit value")
        if len(value) < 8:
            raise serializers.ValidationError("must contain 8 charater")


    def validate_password(self, value):
        """Validate the password meets certain criteria."""
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[a-zA-Z]', value):
            raise serializers.ValidationError("Password must contain letters.")
        if not re.search(r'\d', value):
            raise serializers.ValidationError("Password must contain numbers.")
        if not re.search(r'[!@#$%^&*]', value):
            raise serializers.ValidationError("Password must contain special characters: !@#$%^&*")
        return value

    def validate_fullname(self, value):
        """Validate the format of the full name."""
        if value == "":
            raise serializers.ValidationError("Full name must contain both first and last name.")
        
    def validation(self,value):
        """ Validation for username"""
        
    