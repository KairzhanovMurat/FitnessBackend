from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ReadScheduleSerializer
from core.models import Schedule


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'gym',
                OpenApiTypes.STR,
                description='gym name'
            ),
            OpenApiParameter(
                'trainer',
                OpenApiTypes.STR,
                description='trainers second name'
            )
        ]
    )
)
class ScheduleViewSet(ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ReadScheduleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        gym = self.request.query_params.get('gym')
        trainer = self.request.query_params.get('trainer')
        queryset = self.queryset
        if trainer is not None:
            queryset = queryset.filter(trainer__second_name__icontains=trainer)
        if gym is not None:
            queryset = queryset.filter(gym__name__icontains=gym)
        return queryset.order_by('-id')
