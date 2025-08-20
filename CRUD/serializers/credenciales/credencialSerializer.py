from rest_framework import serializers

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()