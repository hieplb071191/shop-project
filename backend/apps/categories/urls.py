from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.categories.views.admin_view import AdminViews

router = DefaultRouter()
router.register(r'admin-category', AdminViews, basename='admin-category')

urlpatterns = [
    path('', include(router.urls)),
]