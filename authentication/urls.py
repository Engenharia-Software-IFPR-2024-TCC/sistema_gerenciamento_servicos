from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.api.views import AutenticacaoView


router = DefaultRouter()
router.register(r'auth', AutenticacaoView, basename='autenticacao')

urlpatterns = [
    path('', include(router.urls)),
]