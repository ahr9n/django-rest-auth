from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate, password_validation, hashers


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
            "password",
            "password2",
            "date_of_birth",
        )

    def validate_password1(self, data):
        result = password_validation.validate_password(data["password"])
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password doesn't match")
        elif result is None:
            raise serializers.ValidationError("The password is not strong enough")
        else:
            return data

    def validate(self, data):
        self.validate_password1(data)
        return super().validate(data)

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data["name"],
            username=validated_data["email"],
            email=validated_data["email"],
            password=hashers.make_password(validated_data["password"]),
            date_of_birth=validated_data["date_of_birth"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # self.password = hashers.make_password(self.password)
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details!")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "name",
            "email",
            "date_of_birth",
        )
