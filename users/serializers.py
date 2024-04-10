from rest_framework import serializers
from core.models import Trainer, BaseUser, Regular
from gyms.serializers import BaseGymSerializer


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        exclude = (
            'password', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'groups',
            'user_permissions')


class TrainerSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Trainer

    gyms = BaseGymSerializer(many=True, read_only=True)


class RegularSerializer(TrainerSerializer):
    class Meta(TrainerSerializer.Meta):
        model = Regular
