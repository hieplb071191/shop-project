from rest_framework import viewsets

from apps.categories.models import Category
from permisson_guard.role_guard_factory import RoleGuardWith

from apps.categories.serializers import CategorySerializer


class AdminViews(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [RoleGuardWith(['ADMIN'])]