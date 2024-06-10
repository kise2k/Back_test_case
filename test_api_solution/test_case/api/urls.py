from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AdViewSet

router_ver_1 = DefaultRouter()
router_ver_1.register(r'ads', AdViewSet)

urlpatterns = [
    path('', include(router_ver_1.urls)),
]
