from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model().objects.create_user

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
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        user.followers.set(followers_data)
        Token.objects.create(user=user)  # create token on registration
        return user

# Serializer to display user info including followers
class UserSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
