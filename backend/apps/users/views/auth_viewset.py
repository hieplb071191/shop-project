from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.users.serializers import EmailLoginSerializer


class AuthViewSet(viewsets.GenericViewSet):
    serializer_class = EmailLoginSerializer

    @action(detail=False, methods=['post'], url_path=r'login')
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Tạo token JWT
        token = serializer.create_token()
        return Response(token, status=status.HTTP_200_OK)