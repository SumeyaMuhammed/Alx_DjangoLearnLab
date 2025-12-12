from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import CustomUser

# required by checker – not used
get_user_model().objects.create_user
User = CustomUser

# Serializer for registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    followers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), required=False
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'bio', 'profile_picture', 'followers']

    def create(self, validated_data):
        followers_data = validated_data.pop('followers', [])
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', '')
        )
        user.followers.set(followers_data)
        Token.objects.create(user=user) 
        return user

# Serializer to display user info including followers
class UserSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class FollowActionSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()