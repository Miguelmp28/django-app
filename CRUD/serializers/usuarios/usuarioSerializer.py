from rest_framework import serializers
from ...models import Usuarios


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'