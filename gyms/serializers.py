from rest_framework import serializers

from core.models import Gym, BaseUser


class BaseGymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['id', 'name', 'city', 'address']


class ReadGymSerializer(BaseGymSerializer):
    members = serializers.SlugRelatedField(
        slug_field='initials',
        many=True,
        read_only=True
    )

    class Meta(BaseGymSerializer.Meta):
        fields = BaseGymSerializer.Meta.fields + ['members']


class GymsSerializer(BaseGymSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=BaseUser.objects.all(), required=False)

    class Meta(ReadGymSerializer.Meta):
        ...

    def update(self, instance, validated_data):
        members = validated_data.pop('members', [])
        for member in members:
            instance.members.add(member)
        return super().update(instance, validated_data)
