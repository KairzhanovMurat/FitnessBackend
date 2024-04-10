from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Trainer, Regular
from .serializers import TrainerSerializer, RegularSerializer


class TrainerViewSet(ReadOnlyModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class RegularUserViewSet(TrainerViewSet):
    serializer_class = RegularSerializer
    queryset = Regular.objects.all()
