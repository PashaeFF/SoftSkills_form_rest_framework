from rest_framework import serializers, validators
from rest_framework.authtoken.models import Token
from auth2.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=50)
    fullname = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=6, write_only=True)
    
    class Meta():
        model = User
        fields = ('id', 'username', 'fullname', 'email', 'password')

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise validators.ValidationError("Email has already been used")
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user=super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user