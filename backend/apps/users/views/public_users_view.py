

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers

from apps.users.models import User
from apps.users.serializers import UserSerializer

from apps.users.services.users_service import UserService


class PublicUserViewSet(viewsets.GenericViewSet):
    service = UserService
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path=r'get-detail/(?P<user_id>[^/\\]+)')
    def get_user(self, request, user_id=None):
        service_class = self.service()
        print(request.query_params)
        user = service_class.get_user_detail(user_id)
        return Response('1234')

    @action(detail=False, methods=['post'], url_path=r'signup')
    def signup(self, request):
        service_class = self.service()
        return Response(service_class.register_user(request.data))
