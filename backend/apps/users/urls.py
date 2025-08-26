from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users.views  import (PublicUserViewSet)
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views.auth_viewset import AuthViewSet

router = DefaultRouter()
router.register(r'public-users', PublicUserViewSet, basename='public-users')
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
    path('refresh/token', TokenRefreshView.as_view(), name='token_refresh'),
]