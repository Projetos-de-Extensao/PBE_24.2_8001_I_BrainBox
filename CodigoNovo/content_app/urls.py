from rest_framework.routers import DefaultRouter
from .views import MemberViewSet,ConviteViewSet,CadastroViewSet,SistemaViewSet

router = DefaultRouter()

router.register(r'member', MemberViewSet, basename='member')
router.register(r'convite', ConviteViewSet, basename='convite')
router.register(r'cadastro', CadastroViewSet, basename='cadastro')
router.register(r'sistema', SistemaViewSet, basename='sistema')

urlpatterns = router.urls