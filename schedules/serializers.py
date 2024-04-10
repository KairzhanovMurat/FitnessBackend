from rest_framework import serializers

from core.models import Schedule, Regular
from schedules.utils import schedule_check


class BaseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ReadScheduleSerializer(BaseScheduleSerializer):
    gym = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name"
    )

    trainer = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="initials"
    )
    members = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="initials"
    )


class ScheduleSerializer(BaseScheduleSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=Regular.objects.all(), required=False)

    class Meta:
        model = Schedule
        fields = '__all__'

    def create(self, validated_data):
        trainer = validated_data.get('trainer')
        start_time = validated_data.get('start_time')
        end_time = validated_data.get('end_time')
        day = validated_data.get('day')
        gym = validated_data.get('gym')
        schedule_check(trainer=trainer,
                       start_time=start_time,
                       end_time=end_time,
                       day=day,
                       gym=gym,
                       model=Schedule, )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        start_time = validated_data.get('start_time', instance.start_time)
        end_time = validated_data.get('end_time', instance.end_time)
        day = validated_data.get('day', instance.day)
        gym = validated_data.get('gym', instance.gym)
        trainer = validated_data.get('trainer', instance.trainer)
        members = validated_data.pop('members', [])
        for member in members:
            schedule_check(member=member,
                           start_time=start_time,
                           end_time=end_time,
                           day=day,
                           gym=gym,
                           model=Schedule,
                           instance=instance)

            instance.members.add(member)

        schedule_check(trainer=trainer,
                       start_time=start_time,
                       end_time=end_time,
                       day=day,
                       gym=gym,
                       model=Schedule,
                       instance=instance)
        return super().update(instance, validated_data)
