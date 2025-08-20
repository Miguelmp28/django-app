from rest_framework.routers import DefaultRouter
from .views.usuario.usuario import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')


urlpatterns = router.urls