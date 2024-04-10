from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.models import Gym
from .serializers import ReadGymSerializer


class GymViewSet(ReadOnlyModelViewSet):
    serializer_class = ReadGymSerializer
    queryset = Gym.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



