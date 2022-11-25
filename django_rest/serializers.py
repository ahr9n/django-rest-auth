from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
import re


class RegisterSerializer(serializers.ModelSerializer):
    confirmed_password = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "email",
            "password",
            "confirmed_password",
            "date_of_birth",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data["name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            date_of_birth=validated_data["date_of_birth"],
        )
        return user

    def validate(self, data):
        if data["password"] == data["confirmed_password"] and re.match(
            r"^(?=[^\d_].*?\d)\w(\w|[!@#$%]){7,20}", data["password"]
        ):
            return data
        elif not re.match(r"^(?=[^\d_].*?\d)\w(\w|[!@#$%]){7,20}", data["password"]):
            raise serializers.ValidationError("The password is not strong enough")
        else:
            raise serializers.ValidationError("Password doesn't match")


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details!")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "username", "email", "password", "date_of_birth"]


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ["id", "title", "description", "due", "completed"]
        extra_kwargs = {"title": {"required": True}, "due": {"required": True}}

    def create(self, validated_data):
        # more safe
        # user = None
        # request = self.context.get("request")
        # if request and hasattr(request, "user"):
        #     user = request.user
        todos = Todos.objects.create(
            user=self.context.get("request").user,
            title=validated_data["title"],
            description=validated_data["description"],
            completed=validated_data["completed"],
            due=validated_data["due"],
        )
        return todos
