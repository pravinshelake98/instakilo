from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    

class RegistrationSerializer(serializers.Serializer):
    name = serializers.CharField
    emailid = serializers.CharField
    mobno = serializers.IntegerField
    username = serializers.CharField
    password = serializers.CharField