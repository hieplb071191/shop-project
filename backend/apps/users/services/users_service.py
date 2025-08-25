from apps.users.models import User
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from rest_framework.exceptions import ValidationError
from apps.users.dto.user_create_dto import UserSigninDto

from apps.users.serializers import UserSerializer


class UserService:
    model = User


    def get_user_detail(self, user_id):
        user = self.model.objects.filter(id=user_id).values().first()
        if not user:
            raise ValidationError('user not found')
        return user

    def register_user(self, dto):
        user_model = UserSigninDto(data=dto)
        if not user_model.is_valid():
            raise ValidationError(user_model.errors)
        email = dto.get('email')
        old_user = self.model.objects.filter(email=email).first()
        if old_user:
            raise ValidationError('user already exists')

        dto['role'] = self.model.Role.USER
        dto['platform'] = self.model.PlatForm.LOCAL
        dto['is_staff'] = False
        dto['is_superuser'] = False

        print('dto.get', dto.get("extra_fields", {}))

        new_user = self.model.objects.create_user(
            username=dto["username"],
            email=dto["email"],
            password=dto["password"],
            **{k: v for k, v in dto.items() if k not in ["email", "password", "username"]})
        serializer = UserSerializer(new_user)

        return serializer.data