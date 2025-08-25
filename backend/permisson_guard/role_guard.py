from pip._vendor.rich.status import Status
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.permissions import BasePermission
from django.forms.models import model_to_dict
from rest_framework.response import Response

from users.services.users_service import UserService
from http import HTTPStatus


class RoleGuard(BasePermission):
    user_service = UserService

    def __init__(self, role_required=None):
        self.role_required = role_required

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            raise NotAuthenticated({
                'detail': '"Bạn cần đăng nhập để tiếp tục."',
                'status_code': HTTPStatus.UNAUTHORIZED,
            })

        if not self.role_required or len(self.role_required) == 0:
            return True

        if not hasattr(user, "role") or user.role not in self.role_required:
            raise PermissionDenied({
                'status_code': HTTPStatus.FORBIDDEN,
                'default': f"Yêu cầu quyền: {', '.join(self.role_required)}"
            })

        return True