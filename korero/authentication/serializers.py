from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import validators


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(get_user_model().objects.all()),
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(30),
        ]
    )
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )
    email = serializers.EmailField(write_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password',
            'is_staff',
            'first_name',
            'last_name'
        ]
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)

        return user