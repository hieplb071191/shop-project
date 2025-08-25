from apps.users.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Tìm user dựa trên email
        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Email hoặc mật khẩu không đúng")

        user = authenticate(username=user_obj.username, password=password)
        if user is None:
            raise serializers.ValidationError("Email hoặc mật khẩu không đúng")

        attrs['user'] = user
        return attrs

    def create_token(self):
        user = self.validated_data['user']
        refresh = RefreshToken.for_user(user)

        user_data = UserSerializer(user).data
        for key, value in user_data.items():
            refresh[key] = value

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }