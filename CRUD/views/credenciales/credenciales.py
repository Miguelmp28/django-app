from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from ...serializers.credenciales.credencialSerializer import AuthSerializer
from ...service.credenciales.credencialService import AuthService


class Auth(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            token, error = AuthService.autenticar(data['username'], data['password'])

            if error:
                return Response({
                    'error': error
                }, status=status.HTTP_401_UNAUTHORIZED)
            
            return Response(token, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            