from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MonumentViewSet
from .views import register

router = DefaultRouter()
router.register(r'monuments', MonumentViewSet)

urlpatterns = [
    path('register', register),
    path('', include(router.urls)),
]