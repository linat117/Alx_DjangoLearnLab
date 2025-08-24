from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source ="followers.count", read_only = "True")
    following_count = serializers.IntegerField(source = "following.count", read_only = "True")


    class Meta:
        model = User
        fields = [
            "id", "username","email", "bio", "profile_picture", "followers_count", "following_count",
        ]
        read_only_fields = ["id", "followers_count", "following_count"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ["username", "email","password", "bio", "profile_picture"]

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user 
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User 
        fields = ["username", "password"]

    def validate(self, data):
        user = authenticate(username = data.get("username"), password = data.get("password"))
        if not user:
            raise serializers.ValidationError("Invalid Username or password")
        data["user"] = user 
        return data 
    
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields =["email", "bio", "profile_picture"]

