from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import CreateUserSerializer, TokenAuthSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = TokenAuthSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUsersView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreateUserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user



