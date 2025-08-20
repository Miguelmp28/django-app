import hashlib
import jwt
from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from CRUD.models import Credenciales

class AuthService:
    @staticmethod
    def autenticar(username, password):
        try:
            credencial = Credenciales.objects.get(username=username)
        except Credenciales.DoesNotExist:
            return None, 'Usuario no encontrado..!!!'

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if credencial.password != password_hash:
            return None, 'Contraseña incorrecta..!!!'

        payload = {
            'id_usuario': credencial.id_usuario.id_usuario,
            'username': credencial.username,
            'exp': (timezone.now() + timedelta(hours=3)).timestamp()
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return {'access': token}, None
