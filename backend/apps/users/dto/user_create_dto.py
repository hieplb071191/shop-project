from rest_framework import serializers

class UserSigninDto(serializers.Serializer):
    email = serializers.EmailField(max_length=100, required=True)
    password = serializers.CharField(style={'input_type': 'password'}, min_length=8, max_length=32, required=True)
    phone_number = serializers.CharField(style={'input_type': 'phone_number'})
    street_address = serializers.CharField(style={'input_type': 'text'})
    town = serializers.CharField(style={'input_type': 'text'})
    city = serializers.CharField(style={'input_type': 'text'})
    country = serializers.CharField(style={'input_type': 'text'})
