from rest_framework import serializers


def schedule_check(gym, start_time, end_time, day, model, instance=None, trainer=None, member=None):
    target_member = trainer if trainer is not None else member
    if target_member not in gym.members.all():
        raise serializers.ValidationError("User is not a member of the gym")
    conflicting_schedules = model.objects.filter(
        day=day,
        start_time__lt=end_time,
        end_time__gt=start_time,
    ).exclude(pk=instance.pk if instance else None)
    if trainer:
        conflicting_schedules = conflicting_schedules.filter(trainer=trainer)
    if member:
        conflicting_schedules = conflicting_schedules.filter(members=member)
    if conflicting_schedules.exists():
        raise serializers.ValidationError("User has conflicting schedules")
