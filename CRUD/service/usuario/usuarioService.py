from django.shortcuts import get_object_or_404
from ...serializers.usuarios.usuarioSerializer import UsuarioSerializer
from ...models import Usuarios


class UsuarioService:
    @staticmethod
    def listar():
        return Usuarios.objects.all()
    
    @staticmethod
    def obtener_usuario(pk):
        return get_object_or_404(Usuarios, pk=pk)

    @staticmethod
    def crear_usuario(data):
        serializer = UsuarioSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()
    
    @staticmethod
    def actualizar_usuario(pk, data):
        usuario = get_object_or_404(Usuarios, pk=pk)
        serializer = UsuarioSerializer(usuario, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        return serializer.save()
    
    @staticmethod
    def eliminar_usuario(pk):
        usuarios = get_object_or_404(Usuarios, pk=pk)
        usuarios.delete()