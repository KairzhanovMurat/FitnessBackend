from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet

from core.models import Gym, Schedule
from gyms.serializers import GymsSerializer
from schedules.serializers import ScheduleSerializer


class BaseCreateUpdateDeleteViewSet(mixins.CreateModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    GenericViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]


class GymCreateUpdateDeleteViewSet(BaseCreateUpdateDeleteViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymsSerializer


class ScheduleCreateUpdateDeleteViewSet(BaseCreateUpdateDeleteViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

