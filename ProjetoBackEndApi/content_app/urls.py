from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ConviteViewSet, FeedbackViewSet, send_invitation, accept_invitation

router = DefaultRouter()
router.register(r'member_get', ConviteViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = router.urls + [
    path('send-invitation/', send_invitation, name='send_invitation'),
    path('accept-invitation/', accept_invitation, name='accept_invitation'),
]