from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appointment.api.views import AppointmentViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
