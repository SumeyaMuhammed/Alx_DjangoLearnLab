from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserSerializer, FollowActionSerializer

User = get_user_model()
# User Profile
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Register new user
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# Login and return token + user info
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user_data = UserSerializer(token.user).data
        return Response({'token': token.key, 'user': user_data})

class FollowUserView(generics.GenericAPIView):
    serializer_class = FollowActionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'user_id': kwargs.get('user_id')})
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data['user_id']

        try:
            target = self.get_queryset().get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.user == target:
            return Response({'error': "You can't follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target)
        return Response({'status': f'Now following {target.username}'}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    serializer_class = FollowActionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'user_id': kwargs.get('user_id')})
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data['user_id']

        try:
            target = self.get_queryset().get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.remove(target)
        return Response({'status': f'Unfollowed {target.username}'}, status=status.HTTP_200_OK)