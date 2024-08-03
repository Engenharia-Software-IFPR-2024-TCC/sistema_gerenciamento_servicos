from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api.views import ProfileViewSet, FeatureViewSet, RoleViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
