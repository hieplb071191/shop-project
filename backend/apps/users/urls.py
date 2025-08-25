from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users.views  import (PublicUserViewSet)

from users.views.auth_viewset import AuthViewSet

router = DefaultRouter()
router.register(r'public-users', PublicUserViewSet, basename='public-users')
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]