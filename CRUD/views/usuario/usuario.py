from rest_framework import status, viewsets
from rest_framework.response import Response
from ...serializers.usuarios.usuarioSerializer import UsuarioSerializer
from ...service.usuario.usuarioService import UsuarioService


class UsuarioViewSet(viewsets.ViewSet):
    def list(self, request):
        usuarios = UsuarioService.listar()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        usuarios = UsuarioService.crear_usuario(request.data)
        return Response(UsuarioSerializer(usuarios).data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        usuarios = UsuarioService.obtener_usuario(pk)
        serializer = UsuarioSerializer(usuarios)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        usuarios = UsuarioService.actualizar_usuario(pk, request.data)
        return Response(UsuarioSerializer(usuarios).data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        usuarios = UsuarioService.eliminar_usuario(pk)
        return Response(usuarios, status=status.HTTP_204_NO_CONTENT)
