from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users.views  import (PublicUserViewSet)

router = DefaultRouter()
router.register(r'public-users', PublicUserViewSet, basename='public-users')

urlpatterns = [
    path('', include(router.urls)),
]